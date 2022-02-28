from tkinter import *
import requests

api_url = 'https://cowork.asap-it.tech'

status = 0



window = Tk()
window.title("Application B")
window.geometry("400x600")

def task():
    r = requests.get(f'{api_url}/getState/')
    global status
    #status = r

    print(r.json())
    window.after(2000, task)  # reschedule event in 2 seconds

window.after(2000, task)


window.mainloop()
