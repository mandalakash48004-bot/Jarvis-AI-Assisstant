
#client=OpenAI()
 # default to getting the key using os.environ.get("OPENAI_API_KEY")
 #if you saved the key under a different environment variable name , you can do something like:
 # client = OpenAI(
#    api_key =os.environ.get("custom _env_name")
#) pip install openai

## we will install openai then we will get the module of OpenAI from it....and then export it our main program
## we will create client variable through our openai api key.
"""
from google import genai
client=genai.Client(api_key="")
models=client.models.list()
for model in models:
    if "gemini" in model.name.lower():
        print(model.name)

       

import google.generativeai as genai

# Configure your API key
genai.configure(api_key="AIzaSyCszAlew_e3S5SEtr7Se-pGctxuYg0RuO4")

# List all available models
for model in genai.list_models():
    print(model.name)      
    
"""
import pyttsx3
import google.generativeai as genai
import speech_recognition as sr

def ai(command):
# Configure API key
     genai.configure(api_key="AIzaSyCszAlew_e3S5SEtr7Se-pGctxuYg0RuO4")

# Load model
     model = genai.GenerativeModel("models/gemini-2.5-flash")

# Generate response
     response = model.generate_content(command)
     
     engine=pyttsx3.init()
     engine.say(response.text)
     engine.runAndWait()

# Print response
     print(response.text)
r = sr.Recognizer()
with sr.Microphone() as source: ## will listen from source
              print("Listening.....")
              r.adjust_for_ambient_noise(source)### reduce the background noise.
              audio = r.listen(source,timeout=8,phrase_time_limit=9) # the pc will listen to the source and store it in audio,timeout means it will upto that time to start listening.

y=r.recognize_google(audio)
ai(y)




