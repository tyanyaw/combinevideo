#VideoManager.py : handle Video
import os
from typing import Concatenate

from moviepy import VideoFileClip, concatenate_videoclips


#Load Movie Clip Array
def load_video(video_array):

    video_clips = []  # List to hold video objects

    # Loop each video
    for video in video_array:
        
        # Check if the file exists and is non-empty
        if not os.path.exists(video):
            print(f"\nError: {video} does not exist.")
            continue
        
        if os.path.getsize(video) == 0:
            print(f"\nError: {video} is empty.")
            continue

        # Try to load the video
        try:
            clip = VideoFileClip(video)
            print(f"\nLOADING VIDEO: \n    Path         : {video}")
            movie_info(clip)
            video_clips.append(clip) # Append the clip object to the list

        except Exception as e:
            print(f"\nFound Error: Loading video {video}: {e}")

    return video_clips
# End load_video

def movie_info(e):
    print(f"    Name         : {e.filename}")
    print(f"    Duration     : {e.duration}")
    print(f"    Resolution   : {e.size[0]}x{e.size[1]}")
    print(f"    FPS          : {e.fps :.2f}")
    print(f"    Object       : {e}")
# End movie_info

def compositing(list_video):
    composited_clips = []
    try:
        for clip in list_video:
            item = clip.subclipped(0,5)
            composited_clips.append(item)

    except Exception as e:
        print(f"Error in clipping videos: {e}")

    return composited_clips
# End compositing

def combine_video(list_video):

    # Validate input list
    if not list_video or len(list_video)<2:
        print("Error: Need at least two video clips to combine.")
        return

    for clip in list_video:
        print(f"Video to process : {clip.filename}")

    try:
        # Combine the video clips
        print("Video Combining ...")
        combining = concatenate_videoclips(list_video)

        # Preview combined video
        print("Preview Combined Video")
        combining.preview()

        return combining

    except Exception as e:
        print(f"Error while combining videos: {e}")

# End combine_video