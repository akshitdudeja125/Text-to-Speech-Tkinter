# Importing Modules
from tkinter import *
from gtts import gTTS
from playsound import playsound

class TextToSpeech:
    def __init__(self, text,lang):
        self.text = text
        self.lang=lang
        self.speech = gTTS(text=self.text, lang=f"{self.lang}")
        self.speech.save("text.mp3")
        playsound("text.mp3")

def convert(text,l):
  speech=gTTS(text,lang="en")
  speech.save("text.mp3")
  playsound("text.mp3")


main = Tk()
main.geometry("500x500")
main.resizable(height=False, width=False)
main.title("Text to Speech")
main.configure(background="white")

Heading = "Text to Speech Recognizer"
Label(main, text=Heading, font=("Times New Roman", 20, "bold"),bg="white").place(x=47, y=30)

entry = Entry(main, text="Enter",width = 24,bd = 4, font = 14)
entry.place(x = 80, y = 152)
entry.insert(0, "")

btn = Button(main, text = "PLAY",width = "7", pady = 8,font = "bold, 10", bg='yellowgreen',command=convert(entry.get(),"en"))
btn.place(x = 350,y = 145)





main.mainloop()
