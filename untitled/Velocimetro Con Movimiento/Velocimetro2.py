from tkinter import *
from tkinter import ttk
from Speedodom import Speedodom

root = Tk()
f = ttk.Frame()
f.pack()
spd = Speedodom(f, width=400, height=400)
spd.grid(row=0, column=0)

for v in (0,240,0.1):
    spd.setspedd(v)

root.mainloop()



