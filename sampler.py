import os
import glob
import argparse
import random
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', default='/Users/changdae/Desktop/AVS_toy')
parser.add_argument('--out_dir', default='/Users/changdae/Desktop/AVS_test')
parser.add_argument('--num_of_sample', type=int, default=4)
args = parser.parse_args()

all_cropped = sorted(glob.glob(os.path.join(args.data_dir, 'original', 'cropped', '*.mp4')))
all_video_cut = sorted(glob.glob(os.path.join(args.data_dir, 'original', 'video_cut', '*.mp4')))
all_audio_cut = sorted(glob.glob(os.path.join(args.data_dir, 'original', 'audio_cut', '*.wav')))
all_audio_npy = sorted(glob.glob(os.path.join(args.data_dir, 'numpy', 'audio', '*.npy')))

out_cropped_dir = os.path.join(args.out_dir, 'original', 'cropped')
out_video_cut_dir = os.path.join(args.out_dir, 'original', 'video_cut')
out_audio_cut_dir = os.path.join(args.out_dir, 'original', 'audio_cut')
out_audio_npy_dir = os.path.join(args.out_dir, 'numpy', 'audio')

os.makedirs(args.out_dir, exist_ok=True)
os.makedirs(out_cropped_dir, exist_ok=True)
os.makedirs(out_video_cut_dir, exist_ok=True)
os.makedirs(out_audio_cut_dir, exist_ok=True)
os.makedirs(out_audio_npy_dir, exist_ok=True)

if len(all_cropped) != len(all_video_cut) or len(all_video_cut) != len(all_audio_cut) or len(all_audio_cut) != len(all_audio_npy):
    print('Num of data NOT match')
    print('all_cropped:', len(all_cropped))
    print('all_video_cut', len(all_video_cut))
    print('all_audio_cut', len(all_audio_cut))
    print('all_audio_npy', len(all_audio_npy))
    sys.exit()

index_range = range(0, len(all_cropped))
index_list = list(index_range)
sample_idx = random.sample(index_list, args.num_of_sample)

for i, idx in enumerate(sample_idx):
    if i % 1000 == 0:
        print(i, 'is done.')
    out_cropped = os.path.join(out_cropped_dir, os.path.basename(all_cropped[idx]))
    out_video_cut = os.path.join(out_video_cut_dir, os.path.basename(all_video_cut[idx]))
    out_audio_cut = os.path.join(out_audio_cut_dir, os.path.basename(all_audio_cut[idx]))
    out_audio_npy = os.path.join(out_audio_npy_dir, os.path.basename(all_audio_npy[idx]))

    os.rename(all_cropped[idx], out_cropped)
    os.rename(all_video_cut[idx], out_video_cut)
    os.rename(all_audio_cut[idx], out_audio_cut)
    os.rename(all_audio_npy[idx], out_audio_npy)
