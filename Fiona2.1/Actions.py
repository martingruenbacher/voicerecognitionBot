from datetime import datetime
import random
import locale
import wikipedia
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import os


class Actions():

    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
        wikipedia.set_lang("de")

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
        subdirname = os.path.join(dirname, 'vogiwitze')
        files = len([name for name in os.listdir(subdirname) if os.path.isfile(os.path.join(subdirname, name))])
        res = random.randint(1, files)
        filename = os.path.join(subdirname, str(res)+'.mp3')
        playsound(filename)
        return ""
            
