import pyttsx3

engine = pyttsx3.init()
props = engine.getProperty('voices')

for i in range(len(props)):
    print(props[i])
