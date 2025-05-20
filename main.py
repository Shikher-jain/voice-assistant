import os
import time
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from gtts import gTTS
import pygame
from client import client
import musicLibrary

# Initialize pyttsx3 engine once
engine = pyttsx3.init()

newsapi = "cc494a910da1432ab19851bc0d488564"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    temp_path = os.path.join(os.getcwd(), "temp_jarvis.mp3")
    tts = gTTS(text)
    tts.save(temp_path)

    pygame.mixer.init()
    pygame.mixer.music.load(temp_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove(temp_path)

def aiProcess(command):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif command.startswith("play"):
        parts = command.split(" ", 1)
        if len(parts) > 1:
            song = parts[1]
            if song in musicLibrary.music:
                webbrowser.open(musicLibrary.music[song])
            else:
                speak(f"Sorry, I don't have the song {song}.")
        else:
            speak("Please specify the song name.")
    elif "news" in command:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch news right now.")
    else:
        output = aiProcess(command)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            word = recognizer.recognize_google(audio).lower()
            print(f"Heard: {word}")

        
            if word == "hello":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=7, phrase_time_limit=7)
                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(0.5)
