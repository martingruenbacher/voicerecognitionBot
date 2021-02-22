import speech_recognition as sr # speech to text
import pyttsx3 # text to speech
import Brain
from multiprocessing import Process, Queue
import time

 
class Fiona():

    def __init__(self, recordToRecog):
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

    def __init__(self, recordToRecog, recogToAction):
        self.recog = sr.Recognizer()
        self.recordToRecog = recordToRecog
        self.recogToAction = recogToAction

    def recognize(self):
        while True:
            # recognize speech using google
            audio = recordToRecog.get()
            try:
                if audio != None:
                    mytext = self.recog.recognize_google(audio, language='de-DE').lower()
                    print("You have said \n" + mytext)
                    print("Audio Recorded Successfully \n ")
                else:
                    mytext = None
                # process recognized text
                self.recogToAction.put(mytext)
            except Exception as e:
                print("Error :  " + str(e))


class Actions():

    def __init__(self, recogToAction):
        self.recogToActions = recogToAction
        self.cnt = 0
    
    def process(self):
        while True:
            text = self.recogToActions.get()
            if text == None and self.cnt < 5:
                self.cnt += 1
                continue
            else:


if __name__ == "__main__":
    recordToRecog = Queue()
    recogToAction = Queue()

    myFiona = Fiona(recordToRecog)
    myBrain = Brain(recordToRecog, recogToAction)
    myActions = Actions(recogToAction)

    fiona = Process(target=myFiona.listen, args=())
    fiona.start()
    brain = Process(target=myBrain.recognize, args=())
    brain.start()
    actions = Process(target=myActions.process, args=())
    actions.start()
