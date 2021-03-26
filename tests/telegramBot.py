import telepot
from telepot.loop import MessageLoop
from pprint import pprint
import time

CHAT_ID = '-554844776'
bot = telepot.Bot(token='1728199506:AAHqaKqB3Tm5UQ4PJ5zWhxKI6KET1kpvbYo')
print(bot.getMe())
pprint(bot.getUpdates())

# def handle(msg):
#     chat_id = msg['chat']['id']
#     print(chat_id)
#     command = msg['text']
#     print(command)
#     # Martins ID
#     if msg['from']['id'] == 1086734695:
#         bot.sendMessage(chat_id, "You have written: " + command)

#     print('Got command: %s' % command)

# MessageLoop(bot, handle).run_as_thread()
# # necessary for message loop otherwise program will close
# while True:
#     time.sleep(1)

# send photo - works
#bot.sendPhoto(CHAT_ID, photo=open('D:\\Dokumente\\fiona\\voicerecognitionBot\\tests\\resources\\image.jpg', 'rb'))

# send video - works
#bot.sendVideo(CHAT_ID, video=open('D:\\Dokumente\\fiona\\voicerecognitionBot\\tests\\resources\\video.mp4', 'rb'))

# send message - works
#bot.sendMessage(CHAT_ID, "Hallo ihr geilen Säcke!")



