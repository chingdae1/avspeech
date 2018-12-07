import moviepy.editor as mpy
import numpy as np
import librosa


def cut(full_video_path, cut_video_path, full_audio_path, cut_audio_path, start_t, end_t, sr, np_path):
    # Cut video
    myclip = mpy.VideoFileClip(full_video_path)
    subclip = myclip.subclip(start_t, end_t)
    subclip.write_videofile(cut_video_path)

    # Cut audio
    duration = end_t - start_t
    y, _ = librosa.load(full_audio_path, sr, offset=start_t, duration=duration)
    librosa.output.write_wav(cut_audio_path, y, sr)

    # Save audio as numpy
    np.save(np_path, y)
