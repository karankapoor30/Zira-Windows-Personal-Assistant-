import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init("sapi5")  #the pyttsx3.init function access the voices in your system (sapi5 is the default for windows)
voices=engine.getProperty("voices") #to import voices in the code
#print(voices) to know number of voices
#print(voices[1].id)  #to check what is the voice (gender)
engine.setProperty("voice",voices[1].id)   #to set the voice as male or female 1 is for female and 0 is for male

def speak(audio):          #definition to speak
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    elif hour>=16 and hour<21:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("I am Zira. how may I help you today.")

def takeCommand(): #takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source: #takes system microphone as source for listening
        print('Listening...')
        r.pause_threshold=1 #sets the time after microphone stops taking voice input after speech is stopped
        audio=r.listen(source) #this line converts the speech from user into text. this is an attribute of speech recognition
    
    try: #recognizes the speech and converts to text
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(query)

    except Exception as e: #if speech is not recognised this function comes into play
        #print(e)
        print("please say that again...")
        return "None"
    return(query)

def sendEmail(to,content):
    server=smtplib.SMTP("smntp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("your email","your password")
    server.sendmail("your email",to,content)
    server.close()

greetings()
while True:
    query=takeCommand().lower() #speech is converted to all lowercase for easier understanding of system

#this completes the basic speech recognition and vocals of the bot
    if "wikipedia" in query:
        speak("Searching Wikipedia")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        print(results) 
        speak(results)

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com/")
    
    elif "open google" in query:
        webbrowser.open("google.com")

    elif "open stackoverflow" in query:
        webbrowser.open("stackoverflow.com")
    
    elif 'play' in query: #for spotify
        query=query.replace('play','')
        query=query.replace(' ','%20')
        webbrowser.open('https://open.spotify.com/search/'+query)
    
    elif 'on amazon music' in query: #for amazon music
        query=query.replace('on amazon music','')
        query=query.replace(" ","+")
        webbrowser.open("https://music.amazon.in/search/"+query+"?filter=IsLibrary%7Cfalse&sc=none")
    
    elif "the time" in query:
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        speak("the time is"+strtime)
    
    elif "open vs code" in query:
        os.startfile("C:\\Users\\kapoo\\Downloads\\Microsoft VS Code\\Code.exe")
    
    elif "open valorant" in query:
        os.startfile("C:\\Riot Games\\Riot Client\\RiotClientServices.exe --launch-product=valorant --launch-patchline=live")

    elif "send email" in query:
        try:
            speak("who should i send the email to")
            to=takeCommand()
            speak("what should i say")
            content=takeCommand()
            sendEmail(to,content)
            speak("the email has been sent")
        except Exception as e:
            #print(e)
            speak("sorry, i could not send the email")
    



    
    

        

    



