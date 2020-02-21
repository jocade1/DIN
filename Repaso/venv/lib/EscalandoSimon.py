from tkinter import *
from tkinter import ttk
import numpy as np
from EscalaSimon import SimonEscalada


root = Tk()
f = ttk.Frame()
f.pack()
spd =SimonEscalada (f, width=800, height=800)
spd.grid(row=0, column=0)

spd =SimonEscalada (f, width=300, height=300)
spd.grid(row=0, column=1)


root.mainloop()