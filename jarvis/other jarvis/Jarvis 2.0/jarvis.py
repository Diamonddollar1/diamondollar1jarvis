import random
import json
import torch
from brain import NeuralNet
from neuralNetwork import bag_of_words, tokenize
import os

idle_mode = "false"
greet_with_weather = "false"


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
with open("intents.json", "r") as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#-----------------
Name = "Jarvis"

from listen import listen
from speak import say
from task import InputExecution, NonInputExecution
import datetime
import requests
import webbrowser

def wishMe():
    global greet_with_weather
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        say("Good Morning! It is good to see you back!")
    elif hour>=12 and hour<18:
        say("Good Afternoon! It is good to see you back!")
    else:
        say("Good Evening! It is good to see you back!")
    city = "Udaipur"

    def kelvinConvert(kelvin):
        '''
        Converts the Inputed Kelvin Value into Fahrenheit and Celsius.
        '''
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

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

    temp_celsius = round(temp_celsius, 2)
    feels_like_celsius = round(feels_like_celsius, 2)
    
    if greet_with_weather == "true":
        say(f"\nToday, the general weather will be {description}, \nThe temperature is {temp_celsius} degrees Celcius, and It feels like {feels_like_celsius} degrees Celcius outside, \nThe humidity is currently {humidity} percent.")
    else:
        print("NOTE: You have kept Greet with Weather as FALSE")

def Main():
    sentence = listen()
    strSen = str(sentence)

    global idle_mode

    if sentence == "exit":
        exit()
    elif sentence == "idle mode on":
        idle_mode = "true"
    elif sentence == "idle mode off":
        idle_mode = "false"

    sentence = tokenize(sentence)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)

    output = model(x)

    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    checkIdle = True
    if checkIdle == True:
        if idle_mode == "true":
            print("    ")
            print("Could not Reply | Reason:")
            print(f"[STATUS]: Idle_Mode = {idle_mode}\n")
            checkIdle = False

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if idle_mode == "false":
                if tag == intent["tag"]:
                    reply = random.choice(intent["responses"])
                    if reply == "time":
                        NonInputExecution(reply)
                    elif reply == "date":
                        NonInputExecution(reply)
                    elif reply == "day":
                        NonInputExecution(reply)
                    elif reply == "wikipedia":
                        InputExecution(reply, strSen)
                    elif reply == "google":
                        InputExecution(reply, strSen)
                    elif reply == "youtubePlay":
                        InputExecution(reply, strSen)
                    elif reply == "playSong":
                        InputExecution(reply, strSen)
                    elif reply == "youtubeSearch":
                        InputExecution(reply, strSen)
                    else:
                        say(reply)

if __name__ == "__main__":
    wishMe()
    while True:
        Main()