import moviepy.editor
import os
from os.path import isfile, join

files = [f for f in os.listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
for file in files:
    name, ext = os.path.splitext(file)
    if ext == '.mp4' and not os.path.exists(name + '_audio.mp3'):
        video = moviepy.editor.VideoFileClip(file)
        audio = video.audio
        audio.write_audiofile(name + '_audio.mp3')
