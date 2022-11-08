import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print("    ")
            print(f"User: {query}")
        except:
            return ""
        query = str(query)
        return query.lower()




    if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            # extennd the num 2 to increase how much it reads form wiki
            speak("According to Wikipedia")
            print(results)
            speak(results)
            #print(r


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5,phrase_time_limit=5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}")

    except Exception as e:
        # print(e)    
        print("Pardon")  
        return "none"
    return query