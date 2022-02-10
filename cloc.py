from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()

root.title('Digital clock')

def clock():
    tick = strftime('%H:%H:%S %p')

    label.config(text =tick)

    label.after(1000, clock)

label = Label(root, font =('sans', 80), background = 'yellow', foreground = 'orange')
label.pack(anchor= 'center')

clock()
mainloop()