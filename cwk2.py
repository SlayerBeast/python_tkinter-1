from tkinter import *
from subprocess import call
import time
import requests
from bs4 import BeautifulSoup


root = Tk()
mtime = IntVar()

## turn off computer 
def turn_off():
    timez = mtime.get()
    call("shutdown -s -t " + str(timez))
    for i in range(timez):
        label1 = Label(root, text="Your computer will shut down in " + str(timez - i))
        label1.grid(row=3, columnspan=2)
        root.update()
        time.sleep(1)
        

## cancel turning off 		
def cancel_turning_off():
    trigger()
    call("shutdown -a")
    #label1 = Label(root, text=str.replace("Your computer will shut down in ", "You canceled turning off your computer."))
    label1 = Label(root, text="You canceled turning off your computer.")
    label1.grid(row=3, columnspan=2)
    root.update()
    
    
## display public ip using beautifulsoup
def show_ip():
    
    url= 'https://www.google.ie/search?q=ip'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    ip = soup.findAll('div', {'class': '_h4c _rGd vk_h'})
    for item in ip:
        label1 = Label(root, text="Your public ip: " + str(item.text))
        label1.grid(row=3, columnspan=2)
        root.update()

def trigger():
    return True

def quit():
    root.destroy()

button1 = Button(root, text="Turn off computer in ->", fg="green", command=turn_off)
button2 = Button(root, text="Cancel turning off computer.", fg="red", command=cancel_turning_off)
button3 = Button(root, text="Show my public ip", fg="black", command=show_ip)
button4 = Button(root, text="Exit", fg="white", bg="black", command=quit)
entry1 = Entry(root, textvariable=mtime)


button1.grid(row=0, sticky=E)
button2.grid(row=1, columnspan=2)
button3.grid(row=2, columnspan=2)
button4.grid(row=4, sticky=E, column=2)
entry1.grid(row=0, column=1)


root.mainloop()
