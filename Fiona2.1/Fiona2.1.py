import speech_recognition as sr # speech to text
import pyttsx3 # text to speech
from Knowledge import Knowledge
from Actions import Actions
from lib.Telegram import Telegram
from multiprocessing import Process, Queue
import time


# Ear
def listen(recordToRecog):
    recog = sr.Recognizer()
    cnt = 0
    while True:
        with sr.Microphone(device_index=1) as source:
            if cnt > 10:
                recog.adjust_for_ambient_noise(source)
                cnt = 0
            cnt += 1
            print("I am listening")
            audio = recog.listen(source)
            print("Recognizing Now .... ")
            recordToRecog.put(audio)

# Brain
def recognize(recordToRecog, recogToText):
    recog = sr.Recognizer()
    while True:
        # recognize speech using google 
        if recordToRecog.qsize() == 0:
            time.sleep(0.01)
            continue
        audio = recordToRecog.get()
        try:
            if audio != None:
                rec = recog.recognize_google(audio, language='de-DE').lower()
                print("You have said \n" + rec)
                print("Audio Recorded Successfully \n ")
                # process recognized text
                recogToText.put(rec)                
        except Exception as e:
            print("Error :  " + str(e))

# Brain
def getText(recogToText, textToThink):
    cnt = 0
    text = ""
    while True:
        while cnt < 2:
            if recogToText.qsize() == 0:
                cnt += 1
            else:
                text += recogToText.get()
                cnt = 0
            time.sleep(0.5)
        name = ["fiona", "iona", "unna", "jona"]
        if any(x in text for x in name):
            textToThink.put(text)
        cnt = 0
        text = ""

# Brain
def thinkAbout(textToThink):
    voice = Voice()
    teleBot = Telegram()
    action = Actions(teleBot)
    knowledge = Knowledge(action)
    while True:
        # process Fiona input
        if textToThink.qsize() != 0:
            voice.say(knowledge.getKnowledge(textToThink.get()))
        # process TelegramChatBot
        knowledge.checkTelegram(teleBot.getUpdates())
        teleBot.message = ""

        time.sleep(0.01)
          

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
    recogToText = Queue()
    textToThink = Queue()

    ears = Process(target=listen, args=(recordToRecog,))
    ears.start()
    brainRecog = Process(target=recognize, args=(recordToRecog, recogToText))
    brainRecog.start()
    brainText = Process(target=getText, args=(recogToText, textToThink))
    brainText.start()
    brainThink = Process(target=thinkAbout, args=(textToThink,))
    brainThink.start()

