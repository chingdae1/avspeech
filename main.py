import os
import csv
import cv2
import glob
import argparse
import subprocess
from downloader import download
from cutter import cut
from cropper import crop_face


parser = argparse.ArgumentParser()
parser.add_argument('--csv_dir', default='./data_csv')
parser.add_argument('--result_dir', default='./result')
parser.add_argument('--start', default=0, type=int)
parser.add_argument('--end', default=6, type=int)
parser.add_argument('--sr', default=16000)
parser.add_argument('--fourcc', default='avc1')  # In ubuntu, use mp4v for mp4.
parser.add_argument('--crop_ext', default='mp4')
parser.add_argument('--crop_size', default=224)
parser.add_argument('--fps', default=25.0, type=float)
args = parser.parse_args()

all_csv = sorted(glob.glob(os.path.join(args.csv_dir, '*.csv')))

cut_video_dir = os.path.join(args.result_dir, 'original', 'video_cut')
full_video_dir = os.path.join(args.result_dir, 'original', 'video_full')
cut_audio_dir = os.path.join(args.result_dir, 'original', 'audio_cut')
full_audio_dir = os.path.join(args.result_dir, 'original', 'audio_full')
cropped_dir = os.path.join(args.result_dir, 'original', 'cropped')
audio_np_dir = os.path.join(args.result_dir, 'numpy', 'audio')
dummy_dir = os.path.join(args.result_dir, 'dummy')

os.makedirs(args.result_dir, exist_ok=True)
os.makedirs(cut_video_dir, exist_ok=True)
os.makedirs(full_video_dir, exist_ok=True)
os.makedirs(cut_audio_dir, exist_ok=True)
os.makedirs(full_audio_dir, exist_ok=True)
os.makedirs(cropped_dir, exist_ok=True)
os.makedirs(audio_np_dir, exist_ok=True)
os.makedirs(dummy_dir, exist_ok=True)

all_id = []
all_start = []
all_end = []
all_x = []
all_y = []

fail_cnt = 0
done_cnt = 0
skipped_cnt = 0

# Read all CSV
for c in all_csv:
    with open(c, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for col in csv_reader:
            all_id.append(col[0])
            all_start.append(float(col[1]))
            all_end.append(float(col[2]))
            all_x.append(float(col[3]))
            all_y.append(float(col[4]))

print('Sorting..')
zipped = zip(all_id, all_start, all_end, all_x, all_y)
zipped = sorted(zipped)
all_id, all_start, all_end, all_x, all_y = zip(*zipped)

# Check already processed number of data
cnt_path = os.path.join(dummy_dir, 'processed_cnt.txt')
if os.path.exists(cnt_path):
    with open(cnt_path, 'r') as f:
        processed_cnt = int(f.readline())
else:
    with open(cnt_path, 'w') as f:
        f.write('0')
    processed_cnt = 0

all_id = all_id[args.start + processed_cnt:args.end]
all_start = all_start[args.start + processed_cnt:args.end]
all_end = all_end[args.start + processed_cnt:args.end]
all_x = all_x[args.start + processed_cnt:args.end]
all_y = all_y[args.start + processed_cnt:args.end]

prev_id = None
for i in range(len(all_id)):
    id, start, end, x, y = all_id[i], all_start[i], all_end[i], all_x[i], all_y[i]
    print('================== Progress: [{}/{}],  ID:{} =================='.format(i+1, len(all_id), id))
    id_dur = id + '_' + str(int(start)) + '_' + str(int(end))
    id_dur_crop_ext = id_dur + '.' + args.crop_ext
    id_dur_npy = id_dur + '.npy'
    cut_audio_path = os.path.join(cut_audio_dir, id_dur)
    cut_audio_path_ext = cut_audio_path + '.wav'
    full_audio_path = os.path.join(full_audio_dir, id)
    full_audio_path_ext = full_audio_path + '.wav'
    cut_video_path = os.path.join(cut_video_dir, id_dur)
    cut_video_path_ext = cut_video_path + '.mp4'
    full_video_path = os.path.join(full_video_dir, id)
    full_video_path_ext = full_video_path + '.mp4'
    cropped_path = os.path.join(cropped_dir, id_dur_crop_ext)
    audio_np_path = os.path.join(audio_np_dir, id_dur_npy)

    try:
        if id != prev_id and prev_id is not None:
            print('Delete full video, id:', prev_id)
            prev_id_wav = prev_id + '.wav'
            prev_id_mp4 = prev_id + '.mp4'
            prev_audio_full = os.path.join(full_audio_dir, prev_id_wav)
            prev_video_full = os.path.join(full_video_dir, prev_id_mp4)
            if os.path.exists(prev_audio_full):
                os.remove(prev_audio_full)
            if os.path.exists(prev_video_full):
                os.remove(prev_video_full)
        prev_id = id
        # Download full video and audio
        download(id, full_video_path, full_audio_path)

        # Cut out target portion of video and audio
        # Also, save audio as numpy
        cut(full_video_path_ext, cut_video_path_ext,
            full_audio_path_ext, cut_audio_path_ext,
            start, end, args.sr, audio_np_path)

        vc = cv2.VideoCapture(cut_video_path_ext)

        # If FPS is not 25, resample video.
        if vc.get(cv2.CAP_PROP_FPS) != args.fps:
            print('Resample video..')
            fps_int = int(args.fps)
            resample_command = 'ffmpeg -y -i ' + cut_video_path_ext + \
                               ' -r ' + str(fps_int) + \
                               ' -c:v libx264 -b:v 3M -strict -2 -movflags faststart ' \
                               + cut_video_path + '_resampled.mp4'
            subprocess.call(resample_command, shell=True)

            os.remove(cut_video_path_ext)
            os.rename(cut_video_path + '_resampled.mp4', cut_video_path_ext)
            vc.release()
            vc = cv2.VideoCapture(cut_video_path_ext)

        fourcc = cv2.VideoWriter_fourcc(*args.fourcc)
        vid_writer = cv2.VideoWriter(cropped_path,
                                     fourcc,
                                     args.fps,
                                     (args.crop_size, args.crop_size))
        # Crop target face
        is_cropped = crop_face(vc, x, y, vid_writer)
        vc.release()
        vid_writer.release()
        if is_cropped:
            done_cnt += 1
        else:
            print('Skipped:', cropped_path)
            print('REMOVE ALL RELAVANT FILE to', id_dur)
            skipped_cnt += 1
            all_relavant = glob.glob(os.path.join(args.result_dir, '*', '*', id_dur + '*'))
            for f in all_relavant:
                os.remove(f)
    except Exception as e:
        print('[!][!][!][!][!][!][!][!][!][!][!][!][!][!][!]')
        print('FAIL. SOMTHING WRONG. ex) Fail to download.')
        print(e)
        print('REMOVE ALL RELAVANT FILE to', id_dur)
        fail_cnt += 1
        all_relavant = glob.glob(os.path.join(args.result_dir, '*', '*', id_dur + '*'))
        for f in all_relavant:
            os.remove(f)

    # Add count
    with open(cnt_path, 'r') as f:
        cnt = int(f.readline())
    with open(cnt_path, 'w') as f:
        cnt += 1
        f.write(str(cnt))

with open(cnt_path, 'w') as f:
    f.write('0')

print('Done')
print('..')
print('..')
print('========= RESULT =========')
print('Total video:', len(all_id))
print('Preprocessed video:', done_cnt)
print('Failed video:', fail_cnt)
print('Skipped video:', skipped_cnt)
