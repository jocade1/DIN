from tkinter import *
from tkinter import ttk

class MyApp:
  def __init__(self,master):
    button1 = Tkinter.Button(master,text='MuestraTopLevel',command=self.show_window2)
    button1.pack()

  def show_window2(self):
    from FSecondWindow import SecondWin

    t=ttk.Toplevel()
    SecondWin(t)


root=Tk()
app=MyApp(root)
root.mainloop()