import streamlit as st
from audiorecorder import audiorecorder

# pip install streamlit-audiorecorder

# forward 8501
# web visit 127.0.0.1:8501
# 

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.tobytes())
    
    # To save audio to a file:
    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())