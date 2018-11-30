import librosa
import numpy as np

audio_path = '/Users/changdae/Desktop/MARG_Multi_Modal/dataset/result/original/audio/CScH_658uNA.wav'
audio_np_path = '/Users/changdae/Desktop/MARG_Multi_Modal/dataset/result/numpy/audio/CScH_658uNA.npy'
y, _ = librosa.load(audio_path, 16000)
y_np = np.load(audio_np_path)
librosa.output.write_wav('./audio_test.wav', y_np, 16000)