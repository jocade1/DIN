from tkinter import *
from tkinter import ttk
from Tema6.s.SimonEnUnaClase import ClaseSimon

root = Tk()
f = ttk.Frame()
f.pack()
spd = ClaseSimon(f, width=400, height=400)
spd.grid(row=0, column=0)

root.mainloop()

