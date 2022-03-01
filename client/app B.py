import threading

import requests
from tkinter import *
from PIL import Image, ImageTk
from playsound import playsound

from settings import API_URL, DEBUG, FREEZE_WINDOW

r = requests.get(f'{API_URL}/getState/')
status = int(r.json())

color = ['green', 'blue', 'red', 'yellow']

window = Tk()
window.title("Application B")
window.geometry("400x600")
window.resizable(**FREEZE_WINDOW)

img = ImageTk.PhotoImage(Image.open(f'images/image{status}.png').resize((400, 600)))
label = Label(image=img)
l1 = Label(text=status,
           font="Arial 32")
l1.pack(side='top', pady=10)
label.pack(fill='both')


def play_sound(filename):
    playsound(filename)


def task():
    r = requests.get(f'{API_URL}/getState/')
    global status, label
    flag = r.json() != status  # if status changed
    status = r.json()
    img = ImageTk.PhotoImage(Image.open(f'images/image{status}.png').resize((400, 600)))
    label.configure(image=img)
    label.image = img
    x = threading.Thread(target=play_sound, args=[f'sounds/sound{status}.mp3', ])
    if flag:
        x.start()
    l1['text'] = status
    if DEBUG:
        print(r.json())
    window.after(200, task)  # reschedule event in 2 seconds


window.after(200, task)
window.mainloop()
