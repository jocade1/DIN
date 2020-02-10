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

def xy(event):
    global lastx,lasty
    lastx,lasty = cnv.canvasx(event.x), cnv.canvasy(event.y)


root = Tk()


f = ttk.Frame()
f.pack()
cnv = Canvas(f, width=400, height=400)
cnv.grid(row=0, column=0)
#circle_deDentro=[[350,350],[50,50]]
#cnv.create_oval(circle_deDentro)
points_puntero=[[50,203],[201,203]]
cnv.create_line(points_puntero,width= 4.0, fill='blue')


points_short_line=[[0,165],[0,180]]
cnv.create_text([[200,230]],text = "km/h")
circle_deFuera = [[20,20],[380,380]]
cnv.create_oval(circle_deFuera)
circle_delPuntero=[[180,180],[220,220]]
cnv.create_oval(circle_delPuntero,fill="grey")

cnv.bind("<Button-1>", lambda e: print(e.x,e.y))

#Bucle para que aparezcan las lineas largas
points_large_line = [[0,140],[0,180]]
homogenize(points_large_line)
toorig = gettranslation(200, 200)
for rot in range(40,340,20):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = list()
    for i in range(len(points_large_line)):
        temp.append(np.dot(points_large_line[i],transform).tolist())
    dehomogenize(temp)
    cnv.create_line(temp)

#Bucle para lineas cortas

homogenize(points_short_line)
toorig =gettranslation(200,200)
for rot in range(50, 320,10):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = list()
    for i in range(len(points_short_line)):
        temp.append(np.dot(points_short_line[i],transform).tolist())
    #temp.pop(-1)
    dehomogenize(temp)
    cnv.create_line(temp)



#Bucle para velocidades

points_velocidad =[[0,125]]
homogenize(points_velocidad)
toorig = gettranslation(200,200)
vel =0
for rot in range(40, 340,20):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp=list()
    temp.append(np.dot(points_velocidad[0],transform).tolist())
    dehomogenize(temp)
    cnv.create_text(temp, text= str(vel))
    vel = vel +20









root.mainloop()