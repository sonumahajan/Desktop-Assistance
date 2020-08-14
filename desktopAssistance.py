import pyttsx3 # for speeking strings
import datetime #to get the date and time
import speech_recognition as sr # to get the user input from microphone
import wikipedia #to use the wikipedia info
import webbrowser #to open the browser
import os, sys, subprocess #to use computer's file and directory
import smtplib # to send the email
import random # to genrate a random number


def speak(data):
    engine = pyttsx3.init() #creating the engin
    voices = engine.getProperty('voices')   #getting the voices from module
    engine.setProperty('rate', 130)  # setting rate property
    engine.setProperty('voice', voices[2].id)  #setting voice for speak
    engine.say(data)
    engine.runAndWait()
    engine.stop()
   
def wish():    # this function wish you good morning,afternoon and evening according to current time
    nowdate = datetime.datetime.now()
    if nowdate.hour < 12:
        speak("good morning sir")
    elif nowdate.hour > 12 and nowdate.hour < 4:
        speak("good afternoon sir")
    else:
        speak("good evening sir")

def takeCommand():   #this function take user command from microphone and conver into string and return it
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("="*100)
        print("Listening....")
        rec.pause_threshold = 0.5   # increasing a pause it will take some time to comple the sentence
        audio = rec.listen(source)
        try:
            print("Recognizing...")
            query = rec.recognize_google(audio, language='en-in') #setting google audio recognizer for indian language
            print(f"user said: {query}")
        except Exception as e:
            print("say that again please")
            speak("say that again please")
            return "none"
    return query  # return query to condition check

def open_file(filename):
    if sys.platform == "win32":  # for windows users
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"   # for mac and linux users
        subprocess.call([opener, filename])

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your password') # eneter your email and password but you to enable <less secure app> in your email privacy setting
    server.sendmail('your email', to, content)
    server.close()
    

if __name__ == "__main__":
    # speak("hello sir i am sornu's assistance")
    wish()
    print("="*100)

    while True:
        query = takeCommand().lower()
        if 'hello' in query: # condition for hello
            speak("hello sir how are you")

        elif 'wikipedia' in query: # condition for getting info from wikipedia
            speak("searching wikipedia")
            query = query.replace("wikipedia", " ")
            result = wikipedia.summary(query, sentences=2) #getting info of query only two sentences you can get more if you want
            print(result)
            speak("according to wikipedia ")
            speak(result)

        elif 'open youtube' in query: # condition for open youtube
            webbrowser.open("youtube.com")

        elif 'open facebook' in query: # condition for open facebook
            webbrowser.open("facebook.com")

        elif 'open github' in query: # condition for open github
            webbrowser.open("https://github.com/sonumahajan")

        elif 'open codepan' in query: # condition for open codepan
            webbrowser.open("https://codepen.io/dashboard/")

        elif 'open stackoverflow' in query: # condition for open stackoverflow
            webbrowser.open("https://stackoverflow.com/")

        elif 'open google' in query: # condition for open google.com
            webbrowser.open("google.com")

        elif 'play song' in query: # condition for play song
            songDir = '/home/sonu/Desktop/sonu/assistence/songs'  # put here path of your music folder
            songs = os.listdir(songDir)
            song = random.choice(songs)
            print(f"Playing {song}")
            open_file(f"{songDir}/{song}")

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"now the time is {strtime}")
        
        elif 'send email to ' in query:  # < send email to name of persion
            try:
                speak("what should i say")
                content = takeCommand()
                to = " " # eneter the resever's email
                sendEmail(to, content)
                speak("email send")
            except Exception as e:
                speak("sorry, i am not able to send this email")

        elif 'ok buy' in query:
            speak("thank you for using me")
            print("Sonu")

    print("="*100)