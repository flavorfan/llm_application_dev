import streamlit as st
from audiorecorder import audiorecorder
import os

from pathlib import Path
cur_dir : Path = Path(__file__).parent if "__file__" in locals() else Path.cwd()

import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


# pip install streamlit-audiorecorder

# forward 8501
# web visit 127.0.0.1:8501
# 

openai.api_key = os.environ.get('OPENAI_API_KEY')

st.title("Audio Recorder")
audio_buf = audiorecorder("Click to record", "Recording...")

if len(audio_buf) > 0:
    # To play audio in frontend:
    st.audio(audio_buf.tobytes())
    
    # To save audio to a file:
    if 0:
        audio_file_path = f"{cur_dir}/audio.mp3"
        wav_file = open(audio_file_path, "wb")
        wav_file.write(audio_buf.tobytes())

        audio_file= open(audio_file_path, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    else:
        transcript = openai.Audio.transcribe_raw("whisper-1", audio_buf.tobytes(),'audio.mp3')

    st.json(transcript.to_dict())