import speech_recognition as sr # speech to text
import pyttsx3 # text to speech
import Brain
from multiprocessing import Process, Queue
import time

 
class Fiona():

    def __init__(self):
        self.recog = sr.Recognizer()
        self.fiona = pyttsx3.init()
        self.fiona.setProperty('rate', 125)
        self.brain = Brain.Brain()

def listen(q, recog):
    while True:
        with sr.Microphone(device_index=0) as source:
            print("I am listening")
            audio = recog.listen(source)
            q.put(audio)
            

def recoginze(q, recog):
    while True:
        print("Recognizing Now .... ", q.qsize())
        # recognize speech using google
        try:
            mytext = recog.recognize_google(q.get(), language='de-DE').lower()
            #print("You have said \n" + mytext)
            #print("Audio Recorded Successfully \n ")
            print(mytext)
            name = ["fiona", "iona", "unna"]
            # if any(x in mytext for x in name):
            #     # process recognized text
            #     answer = self.think(mytext)
            #     if answer != None:
            #         self.say(answer)
        except Exception as e:
            pass
            print("Error :  " + str(e))


if __name__ == "__main__":
    q = Queue()
    recog = sr.Recognizer()

    listener = Process(target=listen, args=(q,recog))
    listener.start()
    recognizer = Process(target=recoginze, args=(q,recog))
    recognizer.start()
