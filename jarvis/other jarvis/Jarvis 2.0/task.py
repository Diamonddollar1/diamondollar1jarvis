import datetime
from speak import say
import wikipedia
import pywhatkit
import requests
import webbrowser
#Function

#1 - Non-Input Functions
#eg: Time, Date, SpeedTest, etc.

def time():
    time = datetime.datetime.now().strftime("%H:%M")
    say(f"It is {time} right now.")

def date():
    date = datetime.date.today()
    say(f"Today is {date}.")

def day():
    day = datetime.datetime.now().strftime("%A")
    say(f"It is {day} today!")

def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        time()
    elif "date" in query:
        date()
    elif "day" in query:
        day()

#2 - Input Functions
#eg: open Google, Search on Youtube, Wikipedia, etc.

def kelvinConvert(kelvin):
    '''
    Converts the Inputed Kelvin Value into Fahrenheit and Celsius.
    '''
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def getWeather(city):
    '''
    Gets the weather!
    '''
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = open("weather_api_key", "r").read()
    CITY = city
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()

    temp_kelvin = response["main"]["temp"]
    temp_celsius, temp_fahrenheit = kelvinConvert(temp_kelvin)

    feels_like_kelvin = response["main"]["feels_like"]
    feels_like_celsius, feels_like_fahrenheit = kelvinConvert(feels_like_kelvin)
    humidity = response["main"]["humidity"]
    description = response["weather"][0]["description"]

def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("wikipedia","").replace("what is","").replace("who is","").replace("tell me about","")
        try:
            result = wikipedia.summary(name, sentences=3)
            say(f"According to Wikipedia, {result}")
        except Exception as e:
            say(f"Could not search wikipedia for {name}!")

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","").replace("search google", "").replace("google search", "")
        pywhatkit.search(query)

    elif "youtubePlay" in tag:
        query = str(query).replace("youtube", "")
        query = query.replace("youtube play", "").replace("play on youtube", "").replace("play youtube", "").replace("on youtube", "")
        pywhatkit.playonyt(query)

    elif "playSong" in tag:
        query = str(query).replace("play song", "")
        query = query.replace("play the song", "").replace("play a song", "").replace("song", "")
        query = query + " song"
        pywhatkit.playonyt(query)

    elif "youtubeSearch" in tag:
        query = str(query).replace("search on youtube for", "")
        query = query.replace("search on youtube", "").replace("search youtube", "").replace("youtube search", "").replace("on youtube", "")
        query = query.replace(" ", "+")
        yt_URL = "https://youtube.com/results?search_query=" + query + "/"
        webbrowser.open(yt_URL, new=1, autoraise=True)