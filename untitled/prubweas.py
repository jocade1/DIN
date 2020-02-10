from tkinter import *
from tkinter import ttk


root = Tk()

root.option_add('*tearOff', FALSE)
menubar = Menu(root)
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')


root.mainloop()