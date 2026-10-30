# Speech - Text Maths Table
import speech_recognition as sr
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

root = Tk()
root.title("Speech Maths Table")
root.config(bg = "lightblue")

def translate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say a Number")
        audio = r.listen(source)
    try:
        num = r.recognize_google(audio)
    except:
        num = ("Sorry, couldn't get that")
    speechBox.delete(1.0, END)
    speechBox.insert(END, num)

    def mathsBox():
        table = ""
        



speak = Label(root, text = "Say what number you'd like to see a table of.", foreground = "red")
speak.pack(pady = 10)

speechBox = Text(root, width = 10, height = 1)
speechBox.pack(pady = 15)

record = Button(root, text = "Say Number", command = translate)
record.pack()

Mtable = Label(root)
Mtable.pack(pady = 20)

root.mainloop()

