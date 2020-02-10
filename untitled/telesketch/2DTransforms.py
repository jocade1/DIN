from tkinter import *
from tkinter import ttk
import numpy as np



def homogenize(coords: list)-> list:
    for i in range(len(coords)):
        coords[i].append(1)
    return coords


def dehomogenize(coords:list)-> list:
    for i in range(len(coords)):
        coords[i][0] = coords[i][0] / coords[i][2]
        coords[i][1] = coords[i][1] / coords[i][2]
        del coords[i][2]

def gettranslation(tx:float, ty=float)-> list:
    return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]


def getrotation(deg:float)-> list:
    rad = np.radians(deg)
    return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad),0],[0, 0, 1]]



triangle = [[25, 50],[60, 75],[60, 25]]

window = Tk()
f = ttk.Frame()
f.pack()
window.columnconfigure(0,weight=1)
canvas = Canvas(window,relief = RAISED)
canvas.pack()
points = [20,20,20,200,100,200]
cnv = canvas.create_polygon(triangle,fill = "green")
print(gettranslation(50,50))
print(np.array(gettranslation(50,50)))
print(triangle)
homogenize(triangle)
print(triangle[0])
print(np.dot(triangle[0].gettra))




print(triangle)
print(homogenize(triangle))
print(getrotation(cnv))

window.mainloop()