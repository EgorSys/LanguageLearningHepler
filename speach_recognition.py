import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source_mic:
    print("Say something")
    audio = r.listen(source_mic)

    try:
        text = r.recognize_google(audio)
        print(f"You said: \"{text}\"")
    except:
        print("Oops, something went wrong")