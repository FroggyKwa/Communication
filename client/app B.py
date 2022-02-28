from tkinter import *
import requests

api_url = 'https://cowork.asap-it.tech'

status = 0

color = ['green', 'blue', 'red', 'yellow']



window = Tk()
window.title("Application B")
window.geometry("400x600")

l1 = Label(text=status,
           font="Arial 32")

def task():
    r = requests.get(f'{api_url}/getState/')
    global status, l1
    status = r.json()

    l1.config(bg=color[status - 1])
    l1['text'] = status + 1

    print(r.json())
    window.after(200, task)  # reschedule event in 2 seconds

l1.pack()

window.after(200, task)


window.mainloop()
