import os
import moviepy.editor as mpy
import numpy as np
import librosa


def cut(video_path, audio_path, start_t, end_t, sr, np_path):
    print('cutter')
    # Cut video
    myclip = mpy.VideoFileClip(video_path)
    subclip = myclip.subclip(start_t, end_t)
    os.remove(video_path)
    subclip.write_videofile(video_path)

    # Cut audio
    duration = end_t - start_t
    y, _ = librosa.load(audio_path, sr, offset=start_t, duration=duration)
    os.remove(audio_path)
    librosa.output.write_wav(audio_path, y, sr)

    # Save audio as numpy
    np.save(np_path, y)
