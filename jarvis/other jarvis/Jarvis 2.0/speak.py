import pyttsx3

def say(Text):
    engine = pyttsx3.init('nsss')
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 170)
    print("   ")
    print(f"J.A.R.V.I.S.: {Text}\n")
    engine.say(text=Text)
    #print(voices[5].id)
    engine.runAndWait()

#17, 18, 29, 34
