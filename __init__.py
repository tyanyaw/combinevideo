# __init__.py Load from environment variable
import os
from dotenv import load_dotenv

print(">>> Initialize, reading .env")
# Load the environment variables from the .env file
if not load_dotenv():
    print("Warning: .env file not found.")

# Now check if the required environment variables are set
if not os.getenv("FFMPEG_BINARY") or not os.getenv("FFPLAY_BINARY"):
    raise EnvironmentError("FFMPEG_BINARY or FFPLAY_BINARY not set in .env file.")

print(os.getenv("FFMPEG_BINARY"))
print(os.getenv("FFPLAY_BINARY"))

from moviepy.config import check
print(">>> Check moviepy config")
check()
print("...\n")
