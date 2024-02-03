"""
Give commands using microphone and listen for responses.
Different commands to say are for example:
"date"
"time"
"search in wikipedia 'what You want to search' "
"send email"
"search in chrome"
"play songs"
"remember that "  this creates file and saves your request
"do you know anything"  assistant tells the things your wanted to be remembered
"screenshot"
"joke"
"offline "   (this closes program)

**System (OS) commands:
'restart' - to restart pc
'logout' - to logout pc
'shutdown' - to shutdown pc

"""


import pyttsx3
import speech_recognition as sr
import smtplib
import wikipedia
import webbrowser as wb
import datetime
import pyautogui
import random
import pyjokes
import speaks
import os

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I %M %S")
    speak("The current time is.")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak(random.choice(speaks.welcome_backs))
    time()

    date()
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak(random.choice(speaks.good_mornings))
    elif 12 <= hour < 18:
        speak(random.choice(speaks.good_afternoons))
    elif 18 <= hour < 24:
        speak(random.choice(speaks.good_evenings))
    else:
        speak(random.choice(speaks.good_nights))

    speak(random.choice(speaks.at_your_service))
    speak("Please tell me how can I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizning...")
        query = r.recognize_google(audio, language="en-US")
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please.")
        return ""
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("image.png")

def jokes():
    speak(pyjokes.get_joke())

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 465)
    server.ehlo()
    server.starttls()
    server.login("%%%%%@gmail.com", "password")
    server.sendmail("%%%%%e@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "getemail@gmail.com"
                send_email(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send this email")
        elif "search in chrome" in query:
            speak("What should I search for?")
            chromepath = r"C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search)
        elif ("logout" == query) or ("log out" == query):
            os.system("shutdown -l")
        elif ("shutdown" == query) or ("shut down" == query):
            os.system("shutdown /s /t 1")
        elif "restart" == query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir = r"C:\Users\kasutaja\Music"
            songs = os.listdir(songs_dir)
            print(songs[:len(songs)-1])
            speak(f"You have have total {len(songs)-1} song{'s' if len(songs)-1 > 1 else ''}")
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remember that" in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember to" + data)
            with open("remembered.txt", "a") as file:
                file.write(data + "\n")
        elif "do you know anything" in query:
            with open("remembered.txt", "r") as file:
                data = file.readlines()
                speak(f"You said me to remember {len(data)} {'things' if len(data)>1 else 'thing'}")
                for row in data:
                    speak(f"{row.strip()}")
        elif "screenshot" in query:
            screenshot()
            speak("Screenshot has been taken.")
        elif "joke" in query:
            jokes()
        elif "offline" in query:
            speak(random.choice(speaks.goodbyes))
            quit()
