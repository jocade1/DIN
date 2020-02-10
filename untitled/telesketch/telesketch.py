from tkinter import *
from tkinter import ttk


window=Tk()

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def punto():
    global lastx,lasty
    canvasD.cr

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
canvasD=Canvas(window,relief=RAISED,scrollregion=(0, 0, 1000, 1000))
canvasD.pack()
canvasD.configure(background="blue")

canvasC=Canvas(window,relief=RAISED)
canvasC.pack()
canvasC.configure(background="red")
points = [325, 0, 300,25, 350, 25]
uparrow=canvasC.create_polygon(points,fill="black")

points2 = [325, 55, 300,30, 350, 30]
downarrow=canvasC.create_polygon(points2,fill="black")

points3=[0, 25, 25,0, 25, 50]
leftarrow=canvasC.create_polygon(points3,fill="black")

points4=[55, 25, 30,0, 30, 50]
rightarrow=canvasC.create_polygon(points4,fill="black")

canvasC.bind("<Button-1>", lambda e:print(e.x,e.y))
window.update()
window.maxsize(500,340)
window.minsize(300,340)
window.mainloop()

