import os
import csv
import glob
import argparse
from downloader import download
from cutter import cut
import cv2
from cropper import crop_face

parser = argparse.ArgumentParser()
parser.add_argument('--csv_dir', default='./data_csv')
parser.add_argument('--result_dir', default='./result')
parser.add_argument('--start', default=0)
parser.add_argument('--end', default=1)
parser.add_argument('--sr', default=16000)
parser.add_argument('--fourcc', default='avc1')
parser.add_argument('--crop_size', default=224)
parser.add_argument('--fps', default=25.0)
args = parser.parse_args()

all_csv = sorted(glob.glob(os.path.join(args.csv_dir, '*.csv')))

video_dir = os.path.join(args.result_dir, 'original', 'video')
audio_dir = os.path.join(args.result_dir, 'original', 'audio')
cropped_dir = os.path.join(args.result_dir, 'original', 'cropped')
cropped_np_dir = os.path.join(args.result_dir, 'numpy', 'cropped')
audio_np_dir = os.path.join(args.result_dir, 'numpy', 'audio')
os.makedirs(args.result_dir, exist_ok=True)
os.makedirs(video_dir, exist_ok=True)
os.makedirs(audio_dir, exist_ok=True)
os.makedirs(cropped_dir, exist_ok=True)
os.makedirs(cropped_np_dir, exist_ok=True)
os.makedirs(audio_np_dir, exist_ok=True)

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

all_id = all_id[args.start:args.end]
all_start = all_start[args.start:args.end]
all_end = all_end[args.start:args.end]
all_x = all_x[args.start:args.end]
all_y = all_y[args.start:args.end]

for i in range(len(all_id)):
    id, start, end, x, y = all_id[i], all_start[i], all_end[i], all_x[i], all_y[i]
    print('================== Progress: [{}/{}],  ID:{} =================='.format(i+1, len(all_id), id))
    audio_path = os.path.join(audio_dir, id)
    video_path = os.path.join(video_dir, id)
    cropped_path = os.path.join(cropped_dir, id + '.mp4')
    audio_np_path = os.path.join(audio_np_dir, id + '.npy')
    cropped_np_path = os.path.join(cropped_np_dir, id + '.npy')

    try:
        # Download full video and audio
        download(id, video_path, audio_path)

        # Cut out target portion of video and audio
        # Also, save audio as numpy
        cut(video_path + '.mp4', audio_path + '.wav', start, end, args.sr, audio_np_path)

        # Crop target face and save cropped as numpy
        fourcc = cv2.VideoWriter_fourcc(*args.fourcc)
        vc = cv2.VideoCapture(video_path + '.mp4')
        vid_writer = cv2.VideoWriter(cropped_path,
                                     fourcc,
                                     args.fps,
                                     (args.crop_size, args.crop_size))
        is_cropped = crop_face(vc, x, y, vid_writer, cropped_np_path)

        if is_cropped:
            done_cnt += 1
        else:
            print('Skipped:', cropped_path)
            skipped_cnt += 1
            all_relavant = glob.glob(os.path.join(args.result_dir, '*', '*', id + '*'))
            for f in all_relavant:
                os.remove(f)
    except:
        print('[!][!][!][!][!][!][!][!][!][!][!][!][!][!][!]')
        print('FAIL. SOMTHING WRONG. ex) Fail to download.')
        print('REMOVE ALL RELAVANT FILE to', id)
        fail_cnt += 1
        all_relavant = glob.glob(os.path.join(args.result_dir, '*', '*', id + '*'))
        for f in all_relavant:
            os.remove(f)


print('Done')
print('..')
print('..')
print('========= RESULT =========')
print('Total video:', len(all_id))
print('Preprocessed video:', done_cnt)
print('Failed video:', fail_cnt)
print('Skipped video:', skipped_cnt)