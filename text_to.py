import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS
import tempfile
import os

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        tts.save(temp_audio.name)
        st.audio(temp_audio.name, format="audio/mp3")
        os.unlink(temp_audio.name)

# Streamlit UI
st.title("🎤 Speech-to-Text Converter (Google API)")

# File uploader (Upload MP3/WAV)
uploaded_file = st.file_uploader("Upload an Audio File (MP3, WAV)", type=["mp3", "wav"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    # Convert MP3 to WAV if necessary
    audio = AudioSegment.from_file(temp_audio_path)
    wav_temp_path = temp_audio_path + ".wav"
    audio.export(wav_temp_path, format="wav")

    # Recognize speech from WAV file
    with sr.AudioFile(wav_temp_path) as source:
        st.write("🔍 Processing audio...")
        audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data)
            st.success(f"✅ You said: **{text}**")
            text_to_speech(f"You said: {text}")
        except sr.UnknownValueError:
            st.error("❌ Sorry, I couldn't understand the audio.")
        except sr.RequestError:
            st.error("🔌 Check your internet connection.")

    # Cleanup temp files
    os.remove(temp_audio_path)
    os.remove(wav_temp_path)
