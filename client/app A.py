import requests
from tkinter import *
from tkinter.ttk import *

from settings import API_URL, DEBUG, FREEZE_WINDOW

r = requests.get(f'{API_URL}/getState/')
status = int(r.json())

window = Tk()
window.title("Application A")
window.geometry("400x600")
window.resizable(**FREEZE_WINDOW)


def change():
    global status
    status += 1
    status %= 4

    btn['text'] = f'Change value to {(status + 1) % 4}'
    label['text'] = f'Current value is {status}'
    r = requests.post(f'{API_URL}/changeState?num={status}')
    if DEBUG:
        print(r.json(), r.status_code, r.headers, sep='\n')


btn = Button(window, text=f'Change value to {(status + 1) % 4}')
btn.config(command=change)
btn.place(x=100, y=240, width=200, height=60)

label = Label(text=f'Current value is {status}',
              font="Arial 24")
label.place(x=80, y=40)

window.mainloop()
