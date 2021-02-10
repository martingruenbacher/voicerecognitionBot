import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
from datetime import datetime
import random

 
def main():
 
    r = sr.Recognizer()
 
    while True:

        with sr.Microphone(device_index=3) as source:
            r.adjust_for_ambient_noise(source)
            print("I am listening")
            audio = r.listen(source)
            print("Recognizing Now .... ")
    

            # recognize speech using google
            try:
                mytext = r.recognize_google(audio, language='de-DE')
                print("You have said \n" + mytext)
                print("Audio Recorded Successfully \n ")

                # process recognized text
                res = processText(mytext)
                if res != False:
                    playMP3()
            except Exception as e:
                #pass
                print("Error :  " + str(e))

            
def processText(text):

    name = ["Fiona", "fiona, iona"]
    timeWords = ["spät", "viel Uhr", "viel uhr", "Uhrzeit"]
    dateWords = ["datum", "Datum", "welcher Tag", "welchen Tag", "welcher tag", "welchen tag"]
    thanksWords = ["danke", "Danke", "Dankeschön", "dankeschön"]
    mynameWords = ["dein Name", "dein name", "heißt du", "deinen Namen", "deinen namen"]

    if text.find(name[0]) == -1 and text.find(name[1]) == -1:
        #print("Nenn mich beim Namen!")
        return False

    for word in timeWords:
        if text.find(word) != -1:
            getTime()
            print("Es wurde nach der Uhrzeit gefragt!")
            break

    for word in dateWords:
        if text.find(word) != -1:
            getDate()
            print("Es wurde nach dem Datum gefragt!")
            break
    
    for word in thanksWords:
        if text.find(word) != -1:
            yourWelcome()
            print("Es wurde gedankt!")
            break

    for word in mynameWords:
        if text.find(word) != -1:
            myName()
            print("Es wurde nach Namen gefragt!")
            break


def genMP3(text):
    language = 'de'
    myobj = gTTS(text=text, lang=language, slow=False) 
    myobj.save("welcome.mp3")
   
def playMP3():
    playsound("welcome.mp3")
    os.system("del welcome.mp3")


def getTime():
    timeText = datetime.now().time()
    genMP3("Es ist "+str(timeText)[:5])

def getDate():
    weekdays = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    dateText = datetime.now().date()
    weekdayText = datetime.now().weekday()
    genMP3("Heute ist "+weekdays[weekdayText]+" der "+str(dateText)[:10])

def yourWelcome():
    welcome = ["Bitte, hab ich gern gemacht", "Kein Problem", "Gern geschehen", "Immer wieder gern"]
    genMP3(welcome[random.randint(0,3)])

def myName():
    genMP3("Mein Name ist Fiona")


if __name__ == "__main__":
    main()