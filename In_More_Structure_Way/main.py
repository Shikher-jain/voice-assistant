import time
from voice.speaker import speak
from voice.recognizer import listen, recognize
from tasks import process

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            print("Listening for 'Jarvis'...")
            word = recognize(listen()).lower()
            if word == "hey":
                speak("Yes?")
                command = recognize(listen(timeout=7, phrase_time_limit=7))
                print(f"Command: {command}")
                process(command)

        except Exception as e:
            print(f"[ERROR] {e}")
        
        time.sleep(0.5)
