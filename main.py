# Importing Modules
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

# class TextToSpeech:
#     def __init__(self, text, lang):
#         self.text = text
#         self.lang = lang
#         self.speech = gTTS(text=self.text, lang=f"{self.lang}")
#         self.speech.save("text.mp3")
#         playsound("text.mp3")


def speak(text, lan):
    speech = gTTS(text, lang="en", slow=False)
    speech.save("text.mp3")
    print('hi')
    playsound("text.mp3")


root = Tk()
root.geometry("500x500")
root.resizable(height=False, width=False)
root.title("Text to Speech")
root.configure(background="white")

Heading = "Text to Speech Recognizer"
Label(root, text=Heading, font=("Times New Roman", 20, "bold"),
      bg="white", wrap=True, wraplength=450).place(x=47, y=30)


# entry = Entry(root, text="Enter", width=24, bd=4, font=14)
entry = Text(root, width=24, height=4, bd=4, font=14)
entry.place(x=80, y=152)
btn = Button(root, text="PLAY", width="7", pady=8,
             font="bold, 10", bg='yellowgreen', command=lambda: speak(str(entry.get(1.0, END)), 'en'))
btn.place(x=350, y=145)

root.mainloop()
