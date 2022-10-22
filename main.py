import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import schedule
import time
import python_weather
import asyncio
import os



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Im Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'nora' in command:
                command = command.replace('rufus', '')
                print(command)

    except:
        pass
    return command

def run_nora():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('the time is' + time)
            print(time)

    elif 'who is' in command:
        person = command.replace('lookup', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'weather' in query:
        api_key =



while True:
    run_nora()


run_nora()