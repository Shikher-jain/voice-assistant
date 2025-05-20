import webbrowser
import requests
from voice.speaker import speak
from musicLibrary import music

newsapi = "cc494a910da1432ab19851bc0d488564"

def handle_music(song):
    if song in music:
        webbrowser.open(music[song])
    else:
        speak(f"Sorry, I don't have the song {song}.")

def open_website(command):
    sites = {
        "google": "https://google.com",
        "youtube": "https://youtube.com",
        "facebook": "https://facebook.com",
        "linkedin": "https://linkedin.com",
    }
    for name, url in sites.items():
        if name in command:
            webbrowser.open(url)
            return True
    return False

def read_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
    try:
        r = requests.get(url)
        data = r.json()
        articles = data.get("articles", [])
        for article in articles[:5]:
            speak(article['title'])
    except Exception:
        speak("Unable to fetch news right now.")
