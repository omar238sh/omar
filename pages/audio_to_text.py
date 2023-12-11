import streamlit as st
import whisper as ws
from io import BytesIO
import os

st.markdown("Audio to Text")
file = st.file_uploader('Audio file')
button = st.button("Generate Text")

if button and file:
    # Read the content of the file using BytesIO
    file_content = BytesIO(file.read())

    # Save the content to a temporary file
    with open('file.mp3', 'wb') as f:
        f.write(file_content.read())

    model = ws.load_model("large")
    result = model.transcribe('file.mp3')['text']

    st.write(result)
