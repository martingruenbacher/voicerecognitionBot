import speech_recognition as sr # speech to text
import pyttsx3 # text to speech
from Knowledge import Knowledge
from multiprocessing import Process, Queue
import time

 
class Ears():

    def __init__(self, recordToRecog):
        self.recog = sr.Recognizer()
        self.recordToRecog = recordToRecog

    def listen(self):
        while True:
            with sr.Microphone(device_index=1) as source:
                self.recog.adjust_for_ambient_noise(source)
                print("I am listening")
                audio = self.recog.listen(source)
                print("Recognizing Now .... ")
                self.recordToRecog.put(audio)
            

class Brain():

    def __init__(self, recordToRecog):
        self.recog = sr.Recognizer()
        self.knowledge = Knowledge()
        self.voice = Voice()
        self.recordToRecog = recordToRecog
        self.recogToText = Queue()
        self.textToThink = Queue()
        self.cnt = 0
        self.text = ""

    def recognize(self):
        while True:
            # recognize speech using google
            audio = recordToRecog.get()
            try:
                if audio != None:
                    rec = self.recog.recognize_google(audio, language='de-DE').lower()
                    print("You have said \n" + rec)
                    print("Audio Recorded Successfully \n ")
                    # process recognized text
                    self.recogToText.put(rec)                
            except Exception as e:
                print("Error :  " + str(e))

    def getText(self):
        while True:
            while self.cnt < 3:
                if self.recogToText.qsize() == 0:
                    self.cnt += 1
                else:
                    self.text += self.tecogToText.get()
                    self.cnt = 0
                time.sleep(0.5)
            name = ["fiona", "iona", "unna"]
            if any(x in self.text for x in name):
                self.textToThink.put(self.text)

    def thinkAbout(self):
        while True:
            self.voice.say(self.knowledge.getKnowledge(self.textToThink.get()))
          

class Voice():

    def __init__(self):
        self.voice = pyttsx3.init()
        self.voice.setProperty('rate', 125)
        self.voice.say("Hallo ihr geilen Säcke!")
        self.voice.runAndWait()

    def say(self, text):
        self.voice.say(text)
        self.voice.runAndWait()


if __name__ == "__main__":
    recordToRecog = Queue()

    myEars = Ears(recordToRecog)
    myBrain = Brain(recordToRecog)

    ears = Process(target=myEars.listen, args=())
    ears.start()
    brainRecog = Process(target=myBrain.recognize, args=())
    brainRecog.start()
    brainText = Process(target=myBrain.getText, args=())
    brainText.start()
    brainThink = Process(target=myBrain.thinkAbout, args=())
    brainThink.start()
