from tkinter import *
from tkinter import ttk
from F2camara_delegido import Simon

root = Tk()
frame = Frame(root)
frame.pack()
simon= Simon(frame, width=500,height=500)
simon.grid(row=0,column=0)



simon= Simon(frame, width=300,height=300)
simon.grid(row=0,column=1)
root.mainloop()