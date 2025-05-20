from voice.speaker import speak
from client import client
from mycommands import handle_music, open_website, read_news

def ai_chat(command):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant like Jarvis."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def process(command):
    command = command.lower()

    if open_website(command):
        return
    elif "play" in command:
        song = command.replace("play", "").strip()
        handle_music(song)
    elif "news" in command:
        read_news()
    else:
        response = ai_chat(command)
        speak(response)
