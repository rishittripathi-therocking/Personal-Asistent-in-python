import speech_recognition as sr

def take_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("me: ", query + '\n')

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

    
