import audioop
from io import open_code
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
import turtle
import pygame

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Night")


def hey ():
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    running  = True
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running  = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        pygame.display.flip()
    pygame.quit()                
           
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


    

    
                
if __name__ == '__main__':
    speak("Hey i am your personal assistant. what is your name??")
    query = takecommand().lower()
    person = 'hello'+ query
    speak(person)
    Wish()
    speak("What would you like me to do? i can do anything for you like opening insta,facebook,whatsapp,play music , browsing web etc...")
    


   
 

while True:
    query = takecommand().lower()


    if 'wikipedia' in query:
        speak("Searching, Wait a little bit") 
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query) 
        speak("According to Wikipedia")
        speak(results) 
        print(results)


    elif 'youtube' in query:
        webbrowser.open("youtube.com")
    elif 'instagram' in query:
        webbrowser.open("instagram.com") 

    elif 'bye' in query:
        break       
    elif 'time' in query:
        ct = datetime.datetime.now().strftime("%H:%M:%S")
        speak(ct) 
        print(ct)
    elif 'how are you' in query:
        speak("I Am Good . How are You?")
    elif 'hello' in query:
        speak("hi. It's Good to hear from you. i hope you and your loved ones are staying safe and healthy durin this difficult time.")
    elif 'thank you' in query: 
        speak("you're most welcome,anything else you'd like me to do.")
    elif 'yes' in query:
        speak("what would you like me to do ?" )                 
    elif 'joke' in query:
        jok= pyjokes.pyjokes.get_joke()  
        speak(jok)
        print(jok)
    elif 'play' in query:
        song = query.replace('play','')   
        speak('playing' + song)
        pywhatkit.playonyt(song)
    elif ' fun' in query:
        hey()
        
        
       
    
      
    









    
    
   
