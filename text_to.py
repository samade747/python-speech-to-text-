import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    recognizer.adjust_for_ambient_noise(source=source)
    audio = recognizer.listen(source=source)

    def text_to_speech(text):
        tts = gTTS(text=text, lang="en")
        tts.save("audio.mp3")
        playsound("audio.mp3")
    try:
        text = recognizer.recognize_google(audio)
        result = "you said: " + text
        print(result)
        text_to_speech(result)

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Sorry, I couldn't get the results. Please check your internet connection.")
    
