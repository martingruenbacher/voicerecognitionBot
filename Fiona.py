import speech_recognition as sr
from gtts import gTTS # speech to text
import pyttsx3 # text to speech
import Actions

 
class Fiona():

    def __init__(self):
        self.recog = sr.Recognizer()
        self.action = Actions.Actions()
        self.fiona = pyttsx3.init()
        self.fiona.setProperty('rate', 125)
        self.fiona.say("Hallo ihr geilen Säcke!")
        self.fiona.runAndWait()

    def listen(self):
        with sr.Microphone(device_index=1) as source:
            self.recog.adjust_for_ambient_noise(source)
            print("I am listening")
            audio = self.recog.listen(source)
            print("Recognizing Now .... ")
        
        # recognize speech using google
        try:
            mytext = self.recog.recognize_google(audio, language='de-DE').lower()
            print("You have said \n" + mytext)
            print("Audio Recorded Successfully \n ")
            
            name = ["fiona", "iona", "unna"]
            if any(x in mytext for x in name):
                # process recognized text
                answer = self.think(mytext)
                if answer != None:
                    self.say(answer)
        except Exception as e:
            print("Error :  " + str(e))

    def think(self, text):
        timeWords = ["spät", "viel uhr", "viel uhr", "uhrzeit"]
        dateWords = ["datum", "welcher tag", "welchen tag"]
        thanksWords = ["danke", "dankeschön"]
        mynameWords = ["dein name", "heißt du", "deinen namen", "du heißt"]

        for word in timeWords:
            if text.find(word) != -1:
                self.say(self.action.getTime())
                print("Es wurde nach der Uhrzeit gefragt!")
                break

        for word in dateWords:
            if text.find(word) != -1:
                self.say(self.action.getDate())
                print("Es wurde nach dem Datum gefragt!")
                break
        
        for word in thanksWords:
            if text.find(word) != -1:
                self.say(self.action.yourWelcome())
                print("Es wurde gedankt!")
                break

        for word in mynameWords:
            if text.find(word) != -1:
                self.say(self.action.myName())
                print("Es wurde nach Namen gefragt!")
                break

    def say(self, text):
        self.fiona.say(text)
        self.fiona.runAndWait()


if __name__ == "__main__":
    
    myFiona = Fiona()

    while True:
        myFiona.listen()
    