"""
pyttsx3= python text to speech
speech_recognition= used to convert spoken speech into text and work on API's
automate_wikipedia= used to automate and work with the wikipedia
webbrowser= used for to automate webbrowser
smtplib=sending email
os=used to work and interact with operating system
datetime= used to work with date and time

"""

import pyttsx3
import speech_recognition
import wikipedia
import webbrowser
import smtplib
import os
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Converts text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """Greets the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!.. Insha")
    elif 12 <= hour < 18:
        speak("Good Afternoon!... Insha")
    else:
        speak("Good Evening!... Insha")
    speak("Let me know how I can help you. What are you looking for?")

def takecommand():
    """Captures audio input and converts it to text."""
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening to your voice, Insha.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing your voice, Insha.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Dear Insha, you said: {query}\n")
    except Exception as e:
        print("Insha, please say that again.....")
        return "None"
    return query

def sendEmail(to, content):
    """Sends an email to the specified recipient."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('E-mail', 'Password')
        server.sendmail('E-mail', to, content)
        server.close()
        speak("Your email has been sent successfully.")
    except Exception as e:
        print(e)
        speak("Dear Insha, I am unable to send the email. Please address the error.")

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        if 'open wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("I couldn't find anything on Wikipedia. Please try again.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com")
        elif 'open leetcode' in query:
            webbrowser.open("https://leetcode.com")

        elif 'tell me the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Dear Insha, the time is {str_time}")

        elif 'email to other friend' in query:
            try:
                speak("What should I send?")
                content = takecommand()
                to = 'E-mail'
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Dear Insha, I couldn't send the email. Please address the error.")



