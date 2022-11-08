from email.mime import audio
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):

  # voice to text
  def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

try:
        print("Recognizing...")
        query = sr.recognize_google( audio, language='en-in')
        print(f"user: {query}")

except Exception as e :
     speak("Pardon")
def new_func():
    return"none"
def new_func():
    return query

    # to wish
def wish():
        hour = int(datetime.datetime.now().hour)

        if hour>=0 and hour<=12:
            speak("Good Morning Sir")
        elif hour>12 and hour<18:
            speak("Good Afternoon Sir")
        else:
            speak("Good Evening Sir")
        speak("How may i help you")



if __name__ == "__main__":
    wish()



  

