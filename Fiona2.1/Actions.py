from datetime import datetime
import random
import locale
import wikipedia
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import os
from lib.Spotify import Spotify


class Actions():

    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
        wikipedia.set_lang("de")
        self.sp = Spotify()

    def getTime(self):
        timeText = datetime.now().time()
        return "Es ist "+str(timeText)[:5]

    def getDate(self):
        dateText = datetime.now()
        return "Heute ist "+dateText.strftime("%A")+" der "+str(dateText.strftime("%d.%B%Y"))

    def yourWelcome(self):
        welcome = ["Bitte, hab ich gern gemacht", "Kein Problem", "Gern geschehen", "Immer wieder gern"]
        return welcome[random.randint(0,3)]

    def myName(self):
        return "Mein Name ist Fiona"

    def wikiSearch(self, text):
        article = wikipedia.search(text)[0]
        return wikipedia.summary(article, sentences=5)

    def googleSearch(self, text):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        r = requests.get('https://www.google.com/search?q='+text.replace(" ", "%20"), headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        result = soup.find('div', class_='Z0LcW XcVN5d')
        if result != None:
            return result.text
        else:
            return "Ich habe auf Google nichts gefunden!"
    
    def coinflip(self):
        result = random.randint(0,1)
        if result == 0:
            return "kopf"
        else:
            return "zahl"

    def vogiJoke(self):
        dirname = os.path.dirname(__file__)
        subdirname = os.path.join(dirname, 'resources/vogiwitze')
        files = len([name for name in os.listdir(subdirname) if os.path.isfile(os.path.join(subdirname, name))])
        res = random.randint(1, files)
        filename = os.path.join(subdirname, str(res)+'.mp3')
        playsound(filename)
        return ""
            
    def diceRoll(self):
        result = random.randint(1,6)
        return str(result)

    def fartsound(self):
        dirname = os.path.dirname(__file__)
        subdirname = os.path.join(dirname, 'resources/fartsound')
        files = len([name for name in os.listdir(subdirname) if os.path.isfile(os.path.join(subdirname, name))])
        res = random.randint(1, files)
        filename = os.path.join(subdirname, str(res)+'.mp3')
        playsound(filename)
        return ""

    def spPlay(self):
        self.sp.startSong()
        return "Ich habe Spotify gestartet!"

    def spPause(self):
        self.sp.pauseSong()
        return "Ich habe Spotify angehalten!"

    def spSkip(self):
        self.sp.skipSong()
        return "Ich habe auf Spotify ein Lied übersprungen!"

    def spAddToQueue(self, text):
        self.sp.addToQueue(text)
        return "Ich habe " + text + "zur Warteschlange hinzugefügt!"

    def spPlaySong(self, text):
        self.sp.playSong(text)
        return "Ich habe " + text + "gestartet!"

    def spPlayPlaylist(self, text):
        self.sp.playPlaylist(text)
        return "Ich habe " + text + "Playlist gestartet!"

    def spMaxVol(self):
        self.sp.setMaxVolume()
        return "Ich habe die Lautstärke voll aufgedreht!"

    def spMinVol(self):
        self.sp.setMinVolume()
        return "Ich habe die Lautstärke minimiert!"
    
    def birthdaySearch(self, text):
        dirname = os.path.dirname(__file__)
        subdirname = os.path.join(dirname, 'resources/birthday')
        filename = os.path.join(subdirname, 'birthday'+'.txt')
        with open (filename, "r") as file:
            for line in file:
                if text in line:
                    date = file.readline()
        file.close()
        return date
