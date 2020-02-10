from tkinter import *
from tkinter import ttk
import numpy as np


def homogenize(coords: list):
    for i in range(len(coords)):
        coords[i].append(1)

def dehomogenize(coords: list):
    for i in range(len(coords)):
        coords[i][0] = coords[i][0] / coords[i][2]
        coords[i][1] = coords[i][1] / coords[i][2]
        del coords[i][2]

def gettranslation(tx:float, ty:float)->list:
    return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]



def getrotation(deg:float)->list:
    rad = np.radians(deg)
    return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]


root = Tk()

f = ttk.Frame(root)
f.pack()

canvas = Canvas(f, width=500, height=500)
canvas.grid(row=0,column=0)
brujula = [[150-100,150-100],[350+100,350+100]]
canvas.create_oval(brujula,fill='#FFA200')
canvas.create_oval([150-90,150-90],[350+90,350+90],fill="black")
points_line=[[-120,0],[-180,0]]
canvas.create_line(points_line,fill='#FFA200',width=4)



homogenize(points_line)
toorig = gettranslation(250, 250)
for rot in range(0,360,90):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = list()
    for i in range(len(points_line)):
        temp.append(np.dot(points_line[i],transform).tolist())
    dehomogenize(temp)
    canvas.create_line(temp,fill="green",width=4)


point=[[-120,0],[-180,0]]
toorig = gettranslation(260,240)
homogenize(point)
z =0
coordenadas =['W','N','E','S']
for rot in range(0,360,90):
    rotation = getrotation(rot)
    transform = np.dot(rotation,toorig)
    temp = list()
    temp.append(np.dot(point[0],transform).tolist())
    dehomogenize(temp)
    canvas.create_text(temp, text=str(coordenadas[z]),fill="green")
    print(coordenadas)
    z+=1






root.mainloop()