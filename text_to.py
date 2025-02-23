import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
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

# Microphone recording
if st.button("🎙️ Start Recording"):
    with st.spinner("Listening... Speak now!"):
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.success(f"✅ You said: **{text}**")
            text_to_speech(f"You said: {text}")
        except sr.UnknownValueError:
            st.error("❌ Sorry, I couldn't understand the audio.")
        except sr.RequestError:
            st.error("🔌 Check your internet connection.")

# File uploader (Optional: Upload MP3/WAV instead of using the mic)
uploaded_file = st.file_uploader("Or Upload an Audio File (MP3, WAV)", type=["mp3", "wav"])

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



# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# from pydub import AudioSegment
# from pydub.playback import play
# import tempfile
# import os

# # Tell pydub where to find FFmpeg
# AudioSegment.converter = "/usr/bin/ffmpeg"

# # Initialize recognizer
# recognizer = sr.Recognizer()

# # Function to convert text to speech
# def text_to_speech(text):
#     tts = gTTS(text=text, lang="en")
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
#         tts.save(fp.name)
#         audio = AudioSegment.from_file(fp.name, format="mp3")
#         play(audio)
#         os.unlink(fp.name)

# # Streamlit UI
# st.title("🎤 Speech to Text Converter (Upload Audio)")

# # File uploader
# uploaded_file = st.file_uploader("Upload an audio file (MP3, WAV)", type=["mp3", "wav"])

# if uploaded_file:
#     with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
#         temp_audio.write(uploaded_file.read())
#         temp_audio_path = temp_audio.name

#     # Convert MP3 to WAV (if needed)
#     audio = AudioSegment.from_file(temp_audio_path)
#     wav_temp_path = temp_audio_path + ".wav"
#     audio.export(wav_temp_path, format="wav")

#     # Recognize speech from WAV file
#     with sr.AudioFile(wav_temp_path) as source:
#         st.write("🔍 Processing audio...")
#         audio_data = recognizer.record(source)

#         try:
#             text = recognizer.recognize_google(audio_data)
#             st.success(f"✅ You said: **{text}**")
#             text_to_speech(f"You said: {text}")
#         except sr.UnknownValueError:
#             st.error("❌ Sorry, I couldn't understand the audio.")
#         except sr.RequestError:
#             st.error("🔌 Check your internet connection.")

#     # Cleanup temp files
#     os.remove(temp_audio_path)
#     os.remove(wav_temp_path)


# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# from pydub import AudioSegment
# from pydub.playback import play
# import tempfile
# import os

# # Initialize recognizer
# recognizer = sr.Recognizer()

# # Function to convert text to speech
# def text_to_speech(text):
#     tts = gTTS(text=text, lang="en")
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
#         tts.save(fp.name)
#         audio = AudioSegment.from_file(fp.name, format="mp3")
#         play(audio)
#         os.unlink(fp.name)  # Delete temp file

# # Streamlit UI
# st.title("🎤 Speech to Text Converter by samad (Upload Audio)")

# # File uploader
# uploaded_file = st.file_uploader("Upload an audio file (MP3, WAV)", type=["mp3", "wav"])

# if uploaded_file:
#     with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
#         temp_audio.write(uploaded_file.read())
#         temp_audio_path = temp_audio.name

#     # Convert MP3 to WAV (if needed)
#     audio = AudioSegment.from_file(temp_audio_path)
#     wav_temp_path = temp_audio_path + ".wav"
#     audio.export(wav_temp_path, format="wav")

#     # Recognize speech from WAV file
#     with sr.AudioFile(wav_temp_path) as source:
#         st.write("🔍 Processing audio...")
#         audio_data = recognizer.record(source)

#         try:
#             text = recognizer.recognize_google(audio_data)
#             st.success(f"✅ You said: **{text}**")
#             text_to_speech(f"You said: {text}")
#         except sr.UnknownValueError:
#             st.error("❌ Sorry, I couldn't understand the audio.")
#         except sr.RequestError:
#             st.error("🔌 Check your internet connection.")

#     # Cleanup temp files
#     os.remove(temp_audio_path)
#     os.remove(wav_temp_path)


# # import streamlit as st
# # import speech_recognition as sr
# # from gtts import gTTS
# # from pydub import AudioSegment
# # from pydub.playback import play
# # import tempfile
# # import os

# # # Initialize recognizer
# # recognizer = sr.Recognizer()

# # # Function to convert text to speech
# # def text_to_speech(text):
# #     tts = gTTS(text=text, lang="en")

# #     # Save and play audio using pydub
# #     with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
# #         tts.save(fp.name)
# #         audio = AudioSegment.from_file(fp.name, format="mp3")
# #         play(audio)
# #         os.unlink(fp.name)  # Delete the temp file after playing

# # # Streamlit UI
# # st.title("🎤 Speech to Text Converter (Upload Audio)")

# # # File uploader
# # uploaded_file = st.file_uploader("Upload an audio file (WAV, MP3)", type=["wav", "mp3"])

# # if uploaded_file:
# #     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
# #         temp_audio.write(uploaded_file.read())
# #         temp_audio_path = temp_audio.name

# #     # Recognize speech from uploaded audio
# #     with sr.AudioFile(temp_audio_path) as source:
# #         st.write("🔍 Processing audio...")
# #         audio = recognizer.record(source)

# #         try:
# #             text = recognizer.recognize_google(audio)
# #             st.success(f"✅ You said: **{text}**")
# #             text_to_speech(f"You said: {text}")
# #         except sr.UnknownValueError:
# #             st.error("❌ Sorry, I couldn't understand the audio.")
# #         except sr.RequestError:
# #             st.error("🔌 Check your internet connection.")
    
# #     # Remove temporary audio file
# #     os.remove(temp_audio_path)



# # import streamlit as st
# # import speech_recognition as sr
# # from gtts import gTTS
# # from pydub import AudioSegment
# # from pydub.playback import play
# # import tempfile

# # # Initialize recognizer
# # recognizer = sr.Recognizer()

# # # Function to convert text to speech
# # def text_to_speech(text):
# #     tts = gTTS(text=text, lang="en")

# #     # Use a temporary file to save audio
# #     with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
# #         tts.save(fp.name)
# #         audio = AudioSegment.from_file(fp.name, format="mp3")
# #         play(audio)

# # # Streamlit UI
# # st.title("🎤 Speech to Text Converter")

# # # Start recording button
# # if st.button("Start Recording"):
# #     with sr.Microphone() as source:
# #         st.write("🎙️ Listening... Speak now!")
# #         recognizer.adjust_for_ambient_noise(source)
# #         audio = recognizer.listen(source)

# #         try:
# #             text = recognizer.recognize_google(audio)
# #             st.success(f"✅ You said: **{text}**")
# #             text_to_speech(f"You said: {text}")
# #         except sr.UnknownValueError:
# #             st.error("❌ Sorry, I couldn't understand what you said.")
# #         except sr.RequestError:
# #             st.error("🔌 Check your internet connection.")




# # # import speech_recognition as sr
# # # from gtts import gTTS
# # # from playsound import playsound
# # # import os
# # # recognizer = sr.Recognizer()

# # # with sr.Microphone() as source:
# # #     print("Say something:")
# # #     recognizer.adjust_for_ambient_noise(source=source)
# # #     audio = recognizer.listen(source=source)

# # #     def text_to_speech(text):
# # #         tts = gTTS(text=text, lang="en")
# # #         tts.save("audio.mp3")
# # #         playsound("audio.mp3")
# # #     try:
# # #         text = recognizer.recognize_google(audio)
# # #         result = "you said: " + text
# # #         print(result)
# # #         text_to_speech(result)

# # #     except sr.UnknownValueError:
# # #         print("Sorry, I didn't understand that.")
# # #     except sr.RequestError as e:
# # #         print("Sorry, I couldn't get the results. Please check your internet connection.")
    
