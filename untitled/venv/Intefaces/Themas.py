from tkinter import *
from tkinter import ttk

window = Tk()

f = ttk.Frame(window, borderwidth=15, relief="ridge")
f.grid(column=0, row=0, sticky=(N,W,E,S))
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0,weight=1)
l = ttk.Label(f,text="just a test")
l.grid(column=0, row=0)

b = ttk.Button(f,text="just a button")
b.grid(column=0, row = 1)
c = ttk.Checkbutton(f,text = "just a check", varibale= cstr)
c.grid(column=0,row=2)





s = ttk.Style()
stlcar = StringVar()
stl = ttk.Combobox(content,textvariable = stlvar)
stl['values'] = s.theme_names()
selvar.set()
window.mainloop()