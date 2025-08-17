import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configure voice rate and volume (optional)
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def hear():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text.lower()
    except Exception as e:
        print("Error during recognition:", e)
        return ""
