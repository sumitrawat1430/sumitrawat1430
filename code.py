import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser  as wb
import psutil
import pyjokes
import docx
import os
import pyautogui
import random
import wolframalpha
import json
import requests
from urllib.request import urlopen
import time


engine =pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("THE current TIME IS")
    speak(Time)

def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome teamates")
    time_()
    date_()

    hour=datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good morning")
    elif hour >=12 and hour <18:
        speak("Good afternoon sir")
    elif hour >=18 and hour <24:
        speak("Good night sir")
    else :
        speak("Good night sir")
    
    speak("waiting for ur command sir!")


def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listing....")
        r.pause_threshold=1
        audio =r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again.....")
        return "None" 
    return query


def Reading(filename):
    doc =docx.Document(filename)

    completeText=[]
    for pa in doc.paragraphs:
        completeText.append(pa.text)

        return '\n'.join(completeText)

def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()


    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save('D:/New folder (2)/screenshot.png')

def cpu():
    usage=str(psutil.cpu_percent())
    speak('Cpu is at '+usage)
    battery=psutil.sensors_battery()
    speak("battery is ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ =="__main__":
    
    wishme()

    while True:
        query =TakeCommand().lower()

        if 'time' in query:
            time_()
        
        elif 'date' in query:
            date_()
        
        elif 'wikipedia' in query:
            speak('searching....')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("what should i say")
                content=TakeCommand()
                speak("who is the receiver")  
                receiver=input("enter receiver email:")
                to=receiver
                sendmail(to,content)
                speak(content)
                speak('email has sent')


            except Exception as e:
                print(e)
                speak("unable to send")
        
        elif 'search in chrome' in query:

            speak('what should i say')
            search=TakeCommand().lower()
            wb.open(search,new=0,autoraise=True)

        elif 'search youtube' in   query:
            speak('what to search')
            search_term=TakeCommand().lower()
            speak('here we go to youtube')
            wb.open('https://www.youtube.com/result?search_query='+search_term)

        elif 'search google' in query:
            speak('what should i search')
            search_term=TakeCommand().lower()
            speak('Searching.....')
            wb.open('https:www.google.com/search?q='+search_term)


        elif 'cpu enquiry' in query:
            cpu()
        

        elif 'joke' in query:
            jokes()
        
        elif 'go offline' in query:
            speak('going offline sir')
            quit()
        
        elif 'open word file' in query:
            speak(' file name')
            content=TakeCommand()
            print("opening word")
            os.startfile(Reading(content))

        elif 'write a note ' in query:
            speak('what should i write, sir')
            notes =TakeCommand()
            file=open('notes.txt','w')
            speak('sir should i include date and time')
            ans=TakeCommand()
            if 'yes ' in ans or 'sure' in ans :
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("done taking notes")
            else:
                file.write(notes)
        
        elif 'show note ' in query:
            speak('show notes')
            file =open('notes.txt','r')
            print (file.read())
            print(file.write())

        elif 'screenshot' in query:
            screenshot()
        

        elif 'play songs' in query:
            video ='D:/video'
            audio = 'D:/songs'
            speak("What songs should i play? Audio or Video")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())
        
            if 'audio' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)

            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)
                
            speak("select a random number")
            rand = (TakeCommand().lower())
            while('number' not in rand and rand != 'random'):                   
                speak("I could not understand you. Please Try again.")          
                rand = (TakeCommand().lower())

            if 'number' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                                    
            elif 'random' in rand:
                    rand = random.randint(1,219)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue
            
            
            
        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())
        
        elif 'where is ' in query:
            query=query.replace('where is','')
            location=query
            speak("u asked to locate "+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/everything?q=tesla&from=2021-04-27&sortBy=publishedAt&apiKey=c1c4921d05ed42008c60e5579147ad48")
                data = json.load(jsonObj)
                i=1

                speak('here are some top news from the times of india')
                print('''==========v  ===== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e)) 
        

        elif "calculate" in query:
            
            app_id = "LJTJYV-QT72HJ8UKG"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 
        

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("LJTJYV-QT72HJ8UKG")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results") 


        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
