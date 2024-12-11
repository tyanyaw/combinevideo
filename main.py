import sys
import os

# Append the parent directory of the current script to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the package and other modules
import combinevideo  # This will run __init__.py and load the environment variables
from VideoManager import *
from AudioManager import load_audio

duration = 1*60

clip1 = "./video/video1.mp4"
clip2 = "./video/video2.mp4"

audio1 = "./audio/audio1.mp3"
audio2 = "./audio/audio2.mp3"

VideoArray = [clip1, clip2]
AudioArray = [audio1, audio2]

# Call the load_video function from VideoManager
print("--------------- LOAD VIDEO ---------------")
video_clips = load_video(VideoArray)
print("------------------------------------------\n")

composited_clips = None
if video_clips:
    print("--------------- COMPOSITING VIDEO ---------------")
    composited_clips = compositing(video_clips)
    print("------------------------------------------\n")

if composited_clips:
    print("--------------- COMBINE VIDEO ---------------")
    combined_video = combine_video(composited_clips)
    print("------------------------------------------\n")

# Clear clip from memory
for clip in video_clips:
    clip.close()


print("--------------- LOAD AUDIO ---------------")
load_audio(AudioArray)
print("------------------------------------------\n")
