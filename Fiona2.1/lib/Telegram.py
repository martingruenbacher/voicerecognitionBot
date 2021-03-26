import telepot
from telepot.loop import MessageLoop
from pprint import pprint
import time


class Telegram():

    def __init__(self):
        self.CHAT_ID = '-554844776'
        self.TOKEN = '1728199506:AAHqaKqB3Tm5UQ4PJ5zWhxKI6KET1kpvbYo'
        self.bot = telepot.Bot(token=self.TOKEN)
        self.message = ""
        print(self.bot.getMe())
        MessageLoop(self.bot, self.listen).run_as_thread()

    def listen(self, msg):
        self.message = msg
        chat_id = msg['chat']['id']
        print(chat_id)
        command = msg['text']
        print(command)
        # Martins ID
        if msg['from']['id'] == 1086734695:
            self.bot.sendMessage(chat_id, "You have written: " + command)

        print('Got command: %s' % command)

    def sendPhoto(self, path):
        self.bot.sendPhoto(self.CHAT_ID, photo=open(path, 'rb'))

    def sendVideo(self, path):
        self.bot.sendVideo(self.CHAT_ID, video=open(path, 'rb'))

    def sendMessage(self, msg):
        self.bot.sendMessage(self.CHAT_ID, msg)

    def getUpdates(self):
        return self.message