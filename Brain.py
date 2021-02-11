import Actions


class Brain():

    def __init__(self):
        self.action = Actions.Actions()

    def think(self, text):
        timeWords = ["spät", "viel uhr", "viel uhr", "uhrzeit"]
        dateWords = ["datum", "welcher tag", "welchen tag"]
        thanksWords = ["danke", "dankeschön"]
        mynameWords = ["dein name", "heißt du", "deinen namen", "du heißt"]

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
