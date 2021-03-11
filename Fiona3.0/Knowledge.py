import Actions


class Knowledge():

    def __init__(self):
        self.action = Actions.Actions()

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
                
        # Put your code above
        return "Ich habe dich nicht verstanden!"