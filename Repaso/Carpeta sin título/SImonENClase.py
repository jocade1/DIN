from tkinter import *
from tkinter import ttk
import numpy as np
from SimonMig import Simon

root = Tk()
f = ttk.Frame()
f.pack()
spd = Simon(f, width=400, height=400)
spd.grid(row=0, column=0)


spd = Simon(f, width=200, height=200)
spd.grid(row=0, column=1)


root.mainloop()
