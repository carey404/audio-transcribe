from dotenv import load_dotenv
import openai
import sys
import os
from pydub import AudioSegment

# Ensure the env var is set with a 1Password secret reference 
openai.api_key = os.getenv("OPENAI_API_KEY")

def convert_to_mp3(input_file):
    audio = AudioSegment.from_file(input_file)
    output_file = "converted.mp3"
    audio.export(output_file, format="mp3")
    return output_file

# Check that input file was provided
if len(sys.argv) < 2:
    print("Usage: python script.py <audio_file>")
    sys.exit(1)

# Check for mp3 and convert if needed
input_file = sys.argv[1]
if not input_file.endswith(".mp3"):
    input_file = convert_to_mp3(input_file)

# Open the mp3 and call whisper api to transcribe
with open(input_file, "rb") as audio_file:
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript.text)