import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import requests
import os
import time
# speech to text function
def sptext():
    # recognizer as object of Recognizer
    recognizer=sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("LISTENING............")
            recognizer.adjust_for_ambient_noise(source)
            audio=recognizer.listen(source)
            try:
                print("RECOGNIZING.....")
                data=recognizer.recognize_google(audio)
                print(data)
                return data
            except sr.UnknownValueError:
                print("COUNLD NOT UNDERSTAND .....") 
    #sptext()            
#  text to speech function

def speechtx(z): 
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',115)
    engine.say(z)
    engine.runAndWait() 
    #speechtx("WELCOME TO AFFAN'S WORLD!!!!! AFFAN IS THE BEST GUY")
if __name__ == "__main__":
    if "jarvis start" in sptext().lower():
        speechtx("jarvis activated")
        while True:
            data1= sptext().lower()
            if("your name") in data1:
                name="MY NAME IS JARVIS"
                speechtx(name)
            elif("old are you") in data1:
                age="I AM 2 YEARS OLD"   
                speechtx(age)
            elif("time") in data1:
                now1=datetime.datetime.now().strftime("%I%M%p")
                speechtx(now1)   
            elif("youtube") in data1:
                webbrowser.open("https://www.youtube.com/")
                
            elif("web") in data1:
                webbrowser.open("https://www.linkedin.com/in/affan-khan-8aa477171/")
            elif("joke") in data1:
                    joke1=pyjokes.get_joke(language="en",category="neutral")
                    print(joke1)
                    speechtx(joke1)
            elif("play tune") in data1:
                add="D:\TUNES"
                listsong=os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[1]))
            elif("city") in data1:
                city="PUNE"
                url = 'https://wttr.in/{}'.format(city)
                #try:
                data = requests.get(url)
                T = data.text
                #speechtx(T)
                #except:
                    #T = "Error Occurred"
                print(T)
            elif("google") in data1:
                #webbrowser.open("https://www.google.com/search?q=www.google.com&rlz=1C1UEAD_enIN1008IN1008&oq=www.g&gs_lcrp=EgZjaHJvbWUqBwgEEAAYjwIyBggAEEUYOTINCAEQABiDARixAxiABDIQCAIQABiDARixAxiABBiKBTIHCAMQABiABDIHCAQQABiPAjIHCAUQABiPAjIHCAYQABiPAjIGCAcQRRhB0gEJNjY0NWowajE1qAIAsAIA&sourceid=chrome&ie=UTF-8")    
                

                try:
                    from googlesearch import search
                except ImportError: 
                    print("No module named 'google' found")
                
                print("--------SPEAK  TO SEARCH-------")
                query=sptext()
                
                for j in search(query, tld="co.in", num=10, stop=10, pause=2):

                    print(j)
                    #speechtx(j)

            elif("exit")in data1:
                speechtx("THANK YOU FOR USING JARVIS !!!")
                break

            time.sleep(10)
    else:
        speechtx("THANK YOU FOR USING JARVIS !!!")