import os
import speech_recognition as sr
import google.generativeai as genai

from gtts import gTTS

class GRACE:

    def __init__(self, google_api_key):
        genai.configure(api_key=google_api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

    def listen(self,):

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        with microphone as source:
            print("Detecting your voice ...")
            audio_data = recognizer.listen(source)
            print("Done.")

        try:
            text = recognizer.recognize_google(audio_data, language="en-US")
            print(f"You just say - {text}")
        except sr.UnknownValueError:
            print("Plese try again...")
            text = self.listen()
        except sr.RequestError as e:
            print("Plese try again...")
            text = self.listen()
        return text
    
    def speak(self, text, language='en-US', slow=False):
        
        tts = gTTS(text=text, lang=language, slow=slow)
        tts.save("response.mp3")
        os.system("afplay response.mp3")

    def start(self,):
        while True:
            print("\n"+"You:")
            prompt = self.listen()

            response = self.chat.send_message(prompt)
            print("\n"+"Gemini:")
            self.speak(text=response.text)

    def end():
        pass 