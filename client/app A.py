from tkinter import *
import requests

api_url = 'https://cowork.asap-it.tech'

status = 0
def change():
    global status
    status += 1
    status %= 4

    b1['text'] = status + 1
    r = requests.post(f'{api_url}/changeState/?num={status}')





window = Tk()
window.title("Application A")
window.geometry("400x600")

b1 = Button(text=status + 1,
            width=15, height=3)
b1.config(command=change)
b1.pack(side=RIGHT, padx=150, pady=250)

window.mainloop()
