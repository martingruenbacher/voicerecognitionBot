from playsound import playsound
import os

print(len([name for name in os.listdir('.') if os.path.isfile(name)]))
dirname = os.path.dirname(__file__)
print(dirname)
filename = os.path.join(dirname, 'vogiwitze/1.mp3')
playsound(filename)
