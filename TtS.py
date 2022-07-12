from gtts import gTTS
from playsound import playsound

text="Hello World"
speech=gTTS(text)
speech.save("HelloWorld.mp3")

playsound("HelloWorld.mp3")