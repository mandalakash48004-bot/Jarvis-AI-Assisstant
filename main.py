import speech_recognition as sr ## it means that we can use sr for speech_recognition
import webbrowser
import pyttsx3
import musicLibrary
import animelist
import requests
import google.generativeai as genai
#from gtts import gTTS
#import pygame
#import os ### we use it to remove temp.mp3 as it cannot replace the file.




recognizer=sr.Recognizer()  ## variable that represents recognizer package.
engine=pyttsx3.init() ##variable that represents pyttsx3 package.
newsapi="Use your newsapi key here"  ## variable that represents newsapi key.

def speak(text):
    engine.say(text)
    engine.runAndWait()
"""    

def speak_old(text):  ### it is a better version of the free microsoft voice model...we access it tgrough gtts and pygame...it can plauy mjusic also......we get that code from chatgpt.
    tts = gTTS(text)
    tts.save('temp.mp3')  
    
# Initialize pygame mixer
    pygame.mixer.init()

# Load MP3 file
    pygame.mixer.music.load("temp.mp3")   # replace with your file name

# Play the music
    pygame.mixer.music.play()

    

# Keep program running while music plays
    while pygame.mixer.music.get_busy():
     continue  
    os.remove()

"""  
    

def aiprocess(command):
    # Configure API key
    genai.configure(api_key="Use you api key here")  # Replace with your actual API key

# Load model
    model = genai.GenerativeModel("models/gemini-2.5-flash")

# Generate response
    response = model.generate_content(command)
    
    
# Print response
    (print (response.text))
    return response.text



def processCommand(c):
    lowered = c.lower()
    if "open google" in lowered:
        webbrowser.open("https://google.com")
        return True
    elif "open anime" in lowered:
        webbrowser.open("https://hianime.re/home")
        return True
    elif "open facebook" in lowered:
        webbrowser.open("https://facebook.com")
        return True
    elif "open youtube" in lowered:
        webbrowser.open("https://www.youtube.com") ### all these to open webs.
        return True
    
    ######this is the code to get news from newsapi through my api key
    elif "news" in lowered:
        r = requests.get(
            "https://newsapi.org/v2/top-headlines?country=us&apiKey=(YOUR_NEWSAPI_KEY)"
        )
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            if articles:
                for article in articles:
                    speak(article["title"])
            else:
                speak("I could not find any news headlines.")
        else:
            speak("Sorry, I could not fetch news right now.")
        return True

    ### to fetch anime...from animelist
    elif lowered.startswith("ok play"):
        hi = lowered.split(" ")[2]
        see = animelist.anime[hi]
        webbrowser.open(see)
        return True
    
    #### to fetch songs from youtube directly.
    elif lowered.startswith("play"):
        if "play hero" in lowered:
            webbrowser.open("https://youtu.be/uGcsIdGOuZY?si=WY0XyyZ1bIa2KQMY")
        elif "play bluebird" in lowered:
            webbrowser.open("https://youtu.be/ziABaAUq5Ck?si=qmwIUo3WutHJHqYJ")
        else:
            print("not available")
        return True

            #OR(alternative way to open songs)
            # song=c.lower().split(" ")[1]
            # link=musicLibrary.music[song]
            # webbrowser.open(link)        
    else:
        output = aiprocess(c)
        speak(output)
        return True



if __name__ == "__main__":
    speak("Initializing Jarvis.......") 
    # Listen for the wake word "Jarvis"
    # obtain audio from source (speaker of pc)

    while True: ### we used while loop because wewant jarvis to keep going not stop after one time....and true means as long as initializing jarvis is true....the audio will be recorded from the source...means the code will run.

       r = sr.Recognizer()
       print("recognizing")
      
# recognize speech using Sphinx
       try:
           with sr.Microphone() as source: ## will listen from source
              print("Listening.....")
              r.adjust_for_ambient_noise(source)### reduce the background noise.
              audio = r.listen(source,timeout=8,phrase_time_limit=9) # the pc will listen to the source and store it in audio,timeout means it will upto that time to start listening.

           y=r.recognize_google(audio) ## i added it because normally it would repeat what i said...but i also want to print it.
           if"jarvis" in y.lower():  ##to make sure it works properly..it should only be activated when we say jarvis.
               speak("hey buddy") ### at first it got activated by everthing...now its only jarvis.
               with sr.Microphone() as source: ### we did this because now after replying ya...it will take command.
                   print("Jarvis active.....")
                   r.adjust_for_ambient_noise(source)
                   audio = r.listen(source,timeout=8,phrase_time_limit=9) # the pc will listen to the source and store it in audio,timeout means it will upto that time to start listening.

               x = r.recognize_google(audio)
               print("Command",x)
               # it will check after you said something...by saying the same as you.
               processCommand(x)
                   ## we called this func here because we after saying jarvis ..it will say ya...then we can give command...so to process it we used it now .

       
       except sr.UnknownValueError:
           print("Sorry could not understand audio") 
           
           ## if  it doesnt hear it will print this.
       except sr.RequestError as e:
           print(" error; {0}".format(e))      ## for other error.
           ## it showed error as pocketsphinx was not installed. 

       except Exception as e:
           print(e)





 