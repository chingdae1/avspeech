import argparse
import os
import glob

parser = argparse.ArgumentParser()
parser.add_argument('--AVS_dir', default='/workspace2')
args = parser.parse_args()

all_AVS = glob.glob(os.path.join(args.AVS_dir, 'train*'))

for i, avs in enumerate(all_AVS):
    all_npy = glob.glob(os.path.join(avs, 'numpy', 'audio', '*'))
    all_cropped = glob.glob(os.path.join(avs, 'original', 'cropped', '*'))

    is_same = (len(all_npy) ==len(all_cropped))
    print('npy:', len(all_npy), 'cropped:', len(all_cropped), is_same)