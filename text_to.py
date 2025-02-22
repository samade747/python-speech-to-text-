import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    recognizer.adjust_for_ambient_noise(source=source)
    audio = recognizer.listen(source=source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: {}".text)

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Sorry, I couldn't get the results. Please check your internet connection.")
    
