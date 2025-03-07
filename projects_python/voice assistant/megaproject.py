import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recogniser = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.co.in/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)  
    else:
        pass      

if __name__ == "__main__":
    speak("Initialising JARVIS")
    while True:
        r = sr.Recognizer()
        print("Recognising")    
        try:
            with sr.Microphone() as source:
                print("JARVIS IS READY TO HEAR YOU :")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes i can hear you boss")
                with sr.Microphone() as source:
                    print("JARVIS ACTIVE :")
                    audio = r.listen(source)
                    command =  r.recognize_google(audio)
                    
                    processcommand(command)
        except Exception as e:
            print("error; {0}".format(e))    
            