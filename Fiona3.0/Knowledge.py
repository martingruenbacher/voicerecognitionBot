

class Knowledge():

    def __init__(self, action):
        self.action = action

    def getKnowledge(self, text):
        timeWords = ["spät", "viel uhr", "uhrzeit"]
        dateWords = ["datum", "welcher tag", "welchen tag"]
        thanksWords = ["danke", "dankeschön"]
        mynameWords = ["dein name", "heißt du", "deinen namen", "du heißt"]
        wikiWords = ["wikipedia", "wiki", "artikel"]
        googleWords = ["google"]
        coinflipWords = ["münzwurf", "kopf oder zahl"]
        vogiWords = ["vogi", "witz", "joke", "vogel", "kransteiner", "jakob", "voji", "phobie"]
        diceWords = ["würfel", "würfle"]
        fartsoundWords = ["furz", "pups", "kurz"]
        birthdayWords = ["geburtstag"]

        for word in timeWords:
            if text.find(word) != -1:
                print("Es wurde nach der Uhrzeit gefragt!")
                return self.action.getTime()

        for word in dateWords:
            if text.find(word) != -1:
                print("Es wurde nach dem Datum gefragt!")
                return self.action.getDate()
                
        for word in thanksWords:
            if text.find(word) != -1:
                print("Es wurde gedankt!")
                return self.action.yourWelcome()

        for word in mynameWords:
            if text.find(word) != -1:
                print("Es wurde nach Namen gefragt!")
                return self.action.myName()

        for word in wikiWords:
            if text.find(word) != -1:
                print("Es wurde nach einem Wikieintrag gefragt!")
                splittedText = text.split()
                if "nach" in splittedText:
                    return self.action.wikiSearch(text[text.find("nach")+5:])
                elif "wikipedia" in splittedText:
                    return self.action.wikiSearch(text[text.find("wikipedia")+10:])
                else:
                    return "Ich habe dich nicht verstanden!"

        for word in googleWords:
            if text.find(word) != -1:
                print("Es wurde nach einer Googlesuche gefragt!")
                splittedText = text.split()
                if "nach" in splittedText:
                    return self.action.googleSearch(text[text.find("nach")+5:])
                elif "google" in splittedText:
                    return self.action.googleSearch(text[text.find("google")+10:])
                else:
                    return "Ich habe dich nicht verstanden!"
                
        for word in coinflipWords:
            if text.find(word) != -1:
                print("Kopf oder Zahl?")
                return self.action.coinflip()

        for word in vogiWords:
            if text.find(word) != -1:
                print("Es wurde nach Vogiwitz gefragt!")
                return self.action.vogiJoke()

        for word in diceWords:
            if text.find(word) != -1:
                print("Der Würfel wurde geworfen!")
                return self.action.diceRoll()

        for word in fartsoundWords:
            if text.find(word) != -1:
                print("Agehhh, wer war den dass?")
                return self.action.fartsound()
                
        if "spotify" in text:
            return self.checkSpotify(text)

        for word in birthdayWords:
            if text.find(word) != -1:
                print("Es wurde nach einem Geburtstag gefragt")
                splittedText = text.split()
                if "von" in splittedText:
                    return self.action.birthdaySearch(text[text.find("von")+4:])
                elif "hat" in splittedText:
                    return self.action.birthdaySearch(text[text.find("hat")+4:len(text)-11])
                else:
                    return "Ich habe dich nicht verstanden!"

        # Put your code above
        return "Ich habe dich nicht verstanden!"


    def checkSpotify(self, text):
        spPlayWords = ["starten", "starte", "start"]
        spPauseWords = ["stop", "stopp", "pause", "pausieren", "anhalten"]
        spSkipWords = ["skip", "überspringe", "überspringen", "weiter"]
        spAddQueueWords = ["füge", "hinzu", "warteschlange", "queue"]
        spPlaySongWords = ["spiele", "song", "lied", "spiel auf", "spiele auf"]
        spItalienWords = ["italien", "italien playlist", "2020", "italy"]
        spVolMaxWords = ["max", "maximale", "laut", "lauter"]
        spVolMinWords = ["min", "leise", "leiser", "minimal"]

        for word in spPlaySongWords:
            if text.find(word) != -1:
                print("Spotify spiel sofort!")
                return self.action.spPlaySong(text[text.find("spotify")+8:])

        for word in spAddQueueWords:
            if text.find(word) != -1:
                print("Spotify füge etwas zur Queue hinzu!")
                return self.action.spAddToQueue(text[text.find("spotify")+8:])

        for word in spPlayWords:
            if text.find(word) != -1:
                print("Spotify Play!")
                return self.action.spPlay()

        for word in spPauseWords:
            if text.find(word) != -1:
                print("Spotify Pause!")
                return self.action.spPause()

        for word in spSkipWords:
            if text.find(word) != -1:
                print("Spotify Skip!")
                return self.action.spSkip()

        for word in spItalienWords:
            if text.find(word) != -1:
                print("Spotify spiel Italien 2020!")
                return self.action.spPlayPlaylist("Italien 2020")

        for word in spVolMaxWords:
            if text.find(word) != -1:
                print("Spotify dreh Lautstärke max!")
                return self.action.spMaxVol()

        for word in spVolMinWords:
            if text.find(word) != -1:
                print("Spotify dreh Lautstärke min!")
                return self.action.spMinVol()


    def checkTelegram(self, msg):
        if msg == "":
            return ""
        print(msg)
        fotoWords = ["foto", "photo"]
        spotifyWords = []

        text = msg['text'].lower()
        for word in fotoWords:
            if text.find(word) != -1:
                print("Telegram send Foto!")
                #return self.action.telegramSendMessage("Ich mache ein Foto!")
                return self.action.telegramSendPhoto()

        if "spotify" in text:
            return self.checkSpotify(text)

        if "wetter" in text:
            return self.action.telegramSendWeather(msg['from']['first_name'])
