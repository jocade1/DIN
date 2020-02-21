from tkinter import *
from tkinter import ttk

root = Tk()
frame =ttk.Frame(root).grid(row=0,column=0)
notebook = ttk.Notebook(frame)
f1=ttk.Frame(notebook)
f2=ttk.Frame(notebook)
f3=ttk.Frame(notebook)

notebook.add(f1,text="Primero")
notebook.add(f2,text="Segundo")
notebook.add(f3,text="Tercero")
notebook.grid(row=0,column=0)


root.mainloop()