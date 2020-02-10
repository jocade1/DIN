from tkinter import *
from tkinter import ttk
from tkinter import colorchooser, messagebox

def cambiarcolor():
    global label
    color = colorchooser.askcolor(initialcolor='#FF6688')
    if messagebox.askyesno(message='Estas seguro de qye ese color es el que quieres?', icon = 'question',
                           title='Confirmar?'):
        label['background'] = color[1]

root = Tk()
root.rowconfigure(0,weight=1,minsize=20)
root.columnconfigure(0, weight=1)
label= ttk.Label(root, text="Soy el label")
label.grid(row=0,column=0,sticky="NSEW")
ttk.Button(root, text="Cambia el color del label",command=cambiarcolor).grid(row=1, column = 0)

root.mainloop()


