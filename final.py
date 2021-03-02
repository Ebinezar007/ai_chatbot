import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pythoncom

print("Initializing Bot")

MASTER = "Bob"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)


    speak("How may I assist you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Sorry i didn't catch that...")
    return query

speak("Initializing bot...")
wishMe()
query = takeCommand()

#Logic

if query:
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)


    elif 'open youtube' in query:
        webbrowser.open("https:\\www.youtube.com")

    elif 'open google' in query:
        webbrowser.open("https:\\www.google.com")

    elif 'play music' in query:
        music_dir = 'E:\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[3]))

     elif 'open code ' in query:
        codePath = 'A:\\vs code\\Microsoft vs code\\Code.exe'
        os.startfile(codePath)

