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
import requests
import webbrowser

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

    elif 'weather' in command:
        api_key = '1f16f47251d11ce0d8fc5b04733150e6'
        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        city_name = take_command()
        talk(city_name)
        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["code"] != "404":
                y = x["main"]
                current_temp = y["temp"]
                current_press = y["pressure"]
                current_humid = y["humidity"]
                z = x["weather"]
                weather_description = z[0] ["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temp)+"\n atmospheric pressure (in hPa unit) ="+str(current_press) +"\n humidity (in percentage) = " +str(current_humid) +"\n description = " +str(weather_description))
        else:
            talk("City not found")

    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'open you tube' in command:
        webbrowser.open("youtube.com")


while True:
    run_nora()
