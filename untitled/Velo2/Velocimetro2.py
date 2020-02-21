from tkinter import *
from tkinter import ttk
from Speedodom import Speedodom

root = Tk()
f = ttk.Frame()
f.pack()
spd = Speedodom(f, width=200, height=200)
spd.grid(row=0, column=0)

root.mainloop()



