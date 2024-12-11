import os.path

from moviepy import AudioFileClip

#Load Audio Clip Array
def load_audio(audio_array):

    #Loop each audio
    for audio in audio_array:

        # Check if the audio file exist and not empty
        if not os.path.exists(audio):
            print(f"\nAudio File Error : {audio} does not exists.")
            continue

        if os.path.getsize(audio) == 0:
            print(f"\nAudio File Error : {audio} is empty")
            continue

        # Try load the audio
        try:
            audio_clip = AudioFileClip(audio)
            print(f"\nLOADING AUDIO : \n    Path         : {audio}")
            audio_info(audio_clip)

            # Close the audio clip after use
            audio_clip.close()

        except Exception as e:
            print(f"\nFound Error: Loading Audio {audio}: {e}")

# End load_audio

def audio_info(e):
    print(f"    Name         : {e.filename}")
    print(f"    Duration     : {e.duration}")
    print(f"    Channel      : {e.nchannels}")
    print(f"    Freq         : {e.fps :.2f}")
    print(f"    Object       : {e}")

# End audio_info