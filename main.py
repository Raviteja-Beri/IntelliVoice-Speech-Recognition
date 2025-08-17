from modules.speech_io import speak, hear
from modules.intent_detector import get_intent
from services import smart_gpt
import pywhatkit
import datetime

def run():
    speak("How can I assist you today?")
    cmd = hear()
    if not cmd:
        speak("I didn't catch that. Please try again.")
        return

    print("Command:", cmd)
    intent, confidence = get_intent(cmd)

    if confidence >= 0.6:
        if intent == "play_song":
            song = cmd.replace("play", "").strip()
            if song:
                speak(f"Playing {song} on YouTube")
                pywhatkit.playonyt(song)
            else:
                speak("Please specify the song name.")
        elif intent == "get_time":
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}.")
        elif intent == "joke":
            speak("Why don't scientists trust atoms? Because they make up everything!")
        elif intent == "identity":
            speak("I am IntelliVoice, your personal AI voice assistant.")
        else:
            speak("That feature is not yet supported.")
    else:
        reply = smart_gpt(cmd)
        speak(reply)

if __name__ == "__main__":
    run()
