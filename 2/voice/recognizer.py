import speech_recognition as sr

recognizer = sr.Recognizer()

def listen(timeout=5, phrase_time_limit=5):
    with sr.Microphone() as source:
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    return audio

def recognize(audio):
    return recognizer.recognize_google(audio)
