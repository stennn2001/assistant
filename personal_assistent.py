"""
Give commands using microphone and listen for responses.
Different commands to say are for example:
date
time
search in wikipedia 'what You want to search'
send email
search in chrome
offline    (this closes program)

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
import random
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
        elif "offline" in query:
            speak(random.choice(speaks.goodbyes))
            quit()
