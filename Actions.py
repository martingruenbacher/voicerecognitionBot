from datetime import datetime
import random
import locale
import wikipedia


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
