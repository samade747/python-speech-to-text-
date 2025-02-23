import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")

    # Use a temporary file to save audio
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
        tts.save(fp.name)
        audio = AudioSegment.from_file(fp.name, format="mp3")
        play(audio)

# Streamlit UI
st.title("🎤 Speech to Text Converter")

# Start recording button
if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.write("🎙️ Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.success(f"✅ You said: **{text}**")
            text_to_speech(f"You said: {text}")
        except sr.UnknownValueError:
            st.error("❌ Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            st.error("🔌 Check your internet connection.")




# import speech_recognition as sr
# from gtts import gTTS
# from playsound import playsound
# import os
# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Say something:")
#     recognizer.adjust_for_ambient_noise(source=source)
#     audio = recognizer.listen(source=source)

#     def text_to_speech(text):
#         tts = gTTS(text=text, lang="en")
#         tts.save("audio.mp3")
#         playsound("audio.mp3")
#     try:
#         text = recognizer.recognize_google(audio)
#         result = "you said: " + text
#         print(result)
#         text_to_speech(result)

#     except sr.UnknownValueError:
#         print("Sorry, I didn't understand that.")
#     except sr.RequestError as e:
#         print("Sorry, I couldn't get the results. Please check your internet connection.")
    
