# note for me; 1) change voice
# email add document feature
# opean camera not working
# put more songs in songs and beats directory
# connect os
# face recognition
#  change browser
#personalise news not working
#switch window not working

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import wikipedia 
import ntpath
import pyttsx3
import speech_recognition as sr 
import datetime
import webbrowser
import os
import cv2
import sys
import random
from requests import get
import smtplib
import pyjokes
import pywhatkit
import features

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
volume = engine.getProperty('volume')
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 230)
engine.setProperty('volume', 1.80)
engine.runAndWait()

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("How May I Help You")       

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

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=5a44b9a7e12b48f2817d9c7714a646b2'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day=["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"today's {day[i]} news is:", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

def sendEmail(to,content): 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rohansjarvis@gmail.com', 'qpcwsmqriqqknyzs')
    server.sendmail('rohansjarvis@gmail.com', to, content)
    server.close()

def kelvinConvert(kelvin):
    '''
    Converts the Inputed Kelvin Value into Fahrenheit and Celsius.
    '''
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def Pass(pass_inp):

       password = "rohan"

       passss  = str(password)

       if passss==str(pass_inp):

              speak("Access Granted .")

              import Main

       else:
              speak("Access Not Granted .")

def NasaNews(Date):

    speak("Extracting Data From Nasa . ")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params = {'date':str(Date)}
    
    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "E:\\Y O U T U B E\\J A R V I S  S E R I E S\\H O W  T O  M A K E  J A R V I S\\" + str(FileName)

    Path_2 = "E:\\Y O U T U B E\\J A R V I S  S E R I E S\\H O W  T O  M A K E  J A R V I S\\DataBase\\NasaDataBase\\" + str(FileName)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()

    speak(f"Title : {Title}")
    speak(f"According To Nasa : {Info}")


def JARVIS(self):
    wishMe()
    while True:    
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
             speak('Searching in Wikipedia...')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
               # extennd the num 2 to increase how much it reads form wiki
             speak("According to Wikipedia")
             print(results)
             speak(results)
        #print(results)

        elif 'set alarm' in query:
            from Features import Alarm
            speak("sir for when should i set an alarm")
            query = takeCommand()
            Alarm(query)

        elif "search on google" in query:
            query = str(query).replace("google","")
            query = query.replace("search","").replace("search google", "").replace("google search", "")
            speak("what should i search sir")
            query = takeCommand()
            pywhatkit.search(query)
        
        elif "search in google" in query:
            query = str(query).replace("google","")
            query = query.replace("search","").replace("search google", "").replace("google search", "")
            speak("what should i search sir")
            query = takeCommand()
            pywhatkit.search(query)

        elif "search on the google" in query:
            query = str(query).replace("google","")
            query = query.replace("search","").replace("search google", "").replace("google search", "")
            speak("what should i search sir")
            query = takeCommand()
            pywhatkit.search(query)

        elif "search in the google" in query:
            query = str(query).replace("google","")
            query = query.replace("search","").replace("search google", "").replace("google search", "")
            speak("what should i search sir")
            query = takeCommand()
            pywhatkit.search(query)

        elif "search google" in query:
            query = str(query).replace("google","")
            query = query.replace("search","").replace("search google", "").replace("google search", "")
            speak("what should i search sir")
            query = takeCommand()
            pywhatkit.search(query)

        elif  "google search" in query:
            query = str(query).replace("google","")
            query = query.replace("search","").replace("search google", "").replace("google search", "")
            speak("what should i search sir")
            query = takeCommand()
            pywhatkit.search(query)

        elif "search on youtube" in query:
             speak("Sir what should I search")
             query = takeCommand()
             query = str(query).replace("search on youtube for", "")
             query = query.replace("search on youtube", "").replace("search youtube", "").replace("youtube search", "").replace("on youtube", "")
             query = query.replace(" ", "+")
             yt_URL = "https://youtube.com/results?search_query=" + query + "/"
             webbrowser.open(yt_URL, new=1, autoraise=True)

        elif "search in youtube" in query:
             speak("Sir what should I search")
             query = takeCommand()
             query = str(query).replace("search on youtube for", "")
             query = query.replace("search on youtube", "").replace("search youtube", "").replace("youtube search", "").replace("on youtube", "")
             query = query.replace(" ", "+")
             yt_URL = "https://youtube.com/results?search_query=" + query + "/"
             webbrowser.open(yt_URL, new=1, autoraise=True)
        
        elif "search the youtube" in query:
             speak("Sir what should I search")
             query = takeCommand()
             query = str(query).replace("search on youtube for", "")
             query = query.replace("search on youtube", "").replace("search youtube", "").replace("youtube search", "").replace("on youtube", "")
             query = query.replace(" ", "+")
             yt_URL = "https://youtube.com/results?search_query=" + query + "/"
             webbrowser.open(yt_URL, new=1, autoraise=True)

        elif "search youtube" in query:
             speak("Sir what should I search")
             query = takeCommand()
             query = str(query).replace("search on youtube for", "")
             query = query.replace("search on youtube", "").replace("search youtube", "").replace("youtube search", "").replace("on youtube", "")
             query = query.replace(" ", "+")
             yt_URL = "https://youtube.com/results?search_query=" + query + "/"
             webbrowser.open(yt_URL, new=1, autoraise=True)

        elif "youtube search" in query:
             speak("Sir what should I search")
             query = takeCommand()
             query = str(query).replace("search on youtube for", "")
             query = query.replace("search on youtube", "").replace("search youtube", "").replace("youtube search", "").replace("on youtube", "")
             query = query.replace(" ", "+")
             yt_URL = "https://youtube.com/results?search_query=" + query + "/"
             webbrowser.open(yt_URL, new=1, autoraise=True)



        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com") 



        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open anime' in query:
            webbrowser.open("zoro.to")   

        elif 'open manga' in query:
            webbrowser.open("mangareader.to")   

        elif 'open amazon' in query:
            webbrowser.open("amazon.in") 

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com") 

        elif 'open prime' in query:
            webbrowser.open("primevideo.com") 

        elif 'open netflix' in query:
            webbrowser.open("netflix.com") 

        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com") 

        elif 'open github' in query:
            webbrowser.open("github.com") 

        elif "close notepad" in query:
            speak("okay sir, closing notead")
            os.system("taskkill /f /im notepad.exe")

        elif "close notes" in query:
            speak("okay sir, closing notead")
            os.system("taskkill /f /im notepad.exe")

        elif "close code" in query:
            speak("okay sir, closing code")
            os.system("taskkill /f /im Code.exe")

        elif "close visual studio" in query:
            speak("okay sir, closing code")
            os.system("taskkill /f /im Code.exe")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\LENOVO\\Desktop\\All other files\\jarvis\\music'
            songs = os.listdir(music_dir)
            rd= random.choice(songs) 
            os.startfile(os.path.join(music_dir, rd))

        elif 'play the music' in query:
            music_dir = 'C:\\Users\\LENOVO\\Desktop\\All other files\\jarvis\\music'
            songs = os.listdir(music_dir)
            rd= random.choice(songs) 
            os.startfile(os.path.join(music_dir, rd))

        elif 'play my music' in query:
            music_dir = 'C:\\Users\\LENOVO\\Desktop\\All other files\\jarvis\\music'
            songs = os.listdir(music_dir)
            rd= random.choice(songs) 
            os.startfile(os.path.join(music_dir, rd))

        elif 'drop the beat' in query:
            music_dir = 'C:\\Users\\LENOVO\\Desktop\\All other files\\jarvis\\my beats'
            songs = os.listdir(music_dir)
            rd= random.choice(songs) 
            os.startfile(os.path.join(music_dir, rd))

        elif 'drop my beat' in query:
            music_dir = 'C:\\Users\\LENOVO\\Desktop\\All other files\\jarvis\\my beats'
            songs = os.listdir(music_dir)
            rd= random.choice(songs) 
            os.startfile(os.path.join(music_dir, rd))

        elif 'play my beat' in query:
            music_dir = 'C:\\Users\\LENOVO\\Desktop\\All other files\\jarvis\\my beats'
            songs = os.listdir(music_dir)
            rd= random.choice(songs) 
            os.startfile(os.path.join(music_dir, rd))

        elif 'play the beat' in query:
            music_dir = 'C:\\Users\\LENOVO\\Desktop\\All other files\\jarvis\\my beats'
            songs = os.listdir(music_dir)
            rd= random.choice(songs) 
            os.startfile(os.path.join(music_dir, rd))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            date = datetime.date.today()
            speak(f"Today is {date}.")

        elif 'day' in query:
            day = datetime.datetime.now().strftime("%A")
            speak(f"It is {day} today!")

        elif 'temperature' in query:
            tem

        elif 'open code' in query:
            codePath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open visual studio' in query:
            codePath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open notes' in query:
            ntpath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(ntpath)
        
        elif 'open notepad' in query:
            ntpath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(ntpath)   

        elif 'open command prompt' in query:
            os.startfile("start cmd")

        elif 'open cmd' in query:
            os.startfile("start cmd")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0) #0 because using internal camer , if using external switch to 1 , etc
            while True:
              ret, img = cap.read()
              cv2.inshow('', img)
              k = cv2.waitKey(50)
              if k ==27:
                break;
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"your IP address is {ip}")

        elif"tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "close program" in query:
            speak("Thanks for using me Sir. See you later")
            sys.exit()

        elif "exit" in query:
            speak("Thanks for using me Sir. See you later")
            sys.exit()

        elif "exit the program" in query:
            speak("Thanks for using me Sir. See you later")
            sys.exit()


        elif "close the program" in query:
            speak("Thanks for using me Sir. See you later")
            sys.exit()

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "shut down" in query:
            os.system("shutdown /s /t 5")

        elif "shut down system" in query:
            os.system("shutdown /s /t 5")

        elif "shut down my system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart my system" in query:
            os.system("shutdown /s /t 5")

        elif "restart system" in query:
            os.system("shutdown /s /t 5")

        elif "restart" in query:
            os.system("shutdown /s /t 5")

        elif "shut down the computer" in query:
            os.system("shutdown /s /t 5")

        elif "shut down computer" in query:
            os.system("shutdown /s /t 5")

        elif "shut down my computer" in query:
            os.system("shutdown /s /t 5")

        elif "restart the computer" in query:
            os.system("shutdown /s /t 5")

        elif "restart computer" in query:
            os.system("shutdown /s /t 5")

        elif "restart my computer" in query:
            os.system("shutdown /s /t 5")

        elif "sleep" in query:
            os.system("rund1132.exe powerprof.dil,SetSuspendState 0,1,0")

        elif "sleep the system" in query:
            os.system("rund1132.exe powerprof.dil,SetSuspendState 0,1,0")

        elif "sleep system" in query:
            os.system("rund1132.exe powerprof.dil,SetSuspendState 0,1,0")

        elif "sleep my system" in query:
            os.system("rund1132.exe powerprof.dil,SetSuspendState 0,1,0")

        elif "sleep the computer" in query:
            os.system("rund1132.exe powerprof.dil,SetSuspendState 0,1,0")

        elif "sleep computer" in query:
            os.system("rund1132.exe powerprof.dil,SetSuspendState 0,1,0")

        elif "sleep my computer" in query:
            os.system("rund1132.exe powerprof.dil,SetSuspendState 0,1,0")

        elif"tell me some news" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"tell some news" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"tell me the news" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"update me with whats going on " in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"what is going on in news" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"what is going on on news" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"what are todays headlines" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"todays headlines" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"latest headlines" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"todays news" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()
        
        elif"update me with some headlines" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"update me with headlines" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"update me with some headlines" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif"update me with todays headlines" in query:
            speak("Just a minute Sir feteching some of the latest news")
            news()

        elif "email to dad" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "bhaskaran.srinivasan@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "email dad" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "bhaskaran.srinivasan@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif " send email to dad" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "bhaskaran.srinivasan@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "mail to dad" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "bhaskaran.srinivasan@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "mail dad" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "bhaskaran.srinivasan@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "send mail to dad" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "bhaskaran.srinivasan@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "email to mom" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "kalpanab81@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "email mom" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "kalpanab81@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "send email to mom" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "kalpanab81@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "mail to mom" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "kalpanab81@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "mail mom" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "kalpanab81@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "send mail to mom" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "kalpanab81@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "email to rohan" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "email rohan" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "mail rohan" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "send email to rohan" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "mail to rohan" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "send mail to rohan" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "email to myself" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "email myself" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "send email to myself" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "mail to myself" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "send mail to myself" in query:
            try:
                speak("what should I say in the email sir")
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")

        elif "mail myself" in query:
            try:
                content = takeCommand().lower()
                to = "rohanhyd07@gmail.com"
                sendEmail(to,content)
                speak("Email has succesfully sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir the email couldnt be sent")



FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./jarvis.ui")) 

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)