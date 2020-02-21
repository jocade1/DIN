from tkinter import *
from tkinter import ttk
import numpy as np


def homogenize(coords: list):
    for i in range(len(coords)):
        coords[i].append(1)
    return coords


def homogenize2(coords: list):
    for i in range(len(coords)):
        coords[i].append(1)


def dehomogenize(coords: list):
    for i in range(len(coords)):
        coords[i][0] = coords[i][0] / coords[i][2]
        coords[i][1] = coords[i][1] / coords[i][2]
        del coords[i][2]


def gettranslation(tx: float, ty: float) -> list:
    return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]


def getrotation(deg: float) -> list:
    rad = np.radians(deg)
    return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]





root = Tk()
frame=Frame(root)
frame.pack()
canvas = Canvas(frame, width =350, height=350)
canvas.grid(row = 0,column=0)

biggest_circle = [[5, 5], [345, 345]]
canvas.create_oval(biggest_circle,fill='grey')


medium_circle = [[10, 10], [340, 340]]
canvas.create_oval(medium_circle,fill='black')


smallest_circle = [[110, 110], [240, 240]]
canvas.create_oval(smallest_circle,fill='silver')


#Small_concentric_circles

biggest_concentric_circle1= [[165, 180], [185, 200]]
canvas.create_oval(biggest_concentric_circle1, fill='black')

smallest_concentric_circle1 =  [[167, 182], [183, 198]]
canvas.create_oval(smallest_concentric_circle1,fill='red')
canvas.tag_bind(smallest_concentric_circle1,"<Button-1>",lambda e: reset())


biggest_concentric_circle2= [[165-35, 180], [185-35, 200]]
canvas.create_oval(biggest_concentric_circle2, fill='black')

smallest_concentric_circle2 =  [[167-35, 182], [183-35, 198]]
canvas.create_oval(smallest_concentric_circle2,fill='yellow')



biggest_concentric_circle3= [[165+35, 180], [185+35, 200]]
canvas.create_oval(biggest_concentric_circle3, fill='black')

smallest_concentric_circle3 =  [[167+35, 182], [183+35, 198]]
canvas.create_oval(smallest_concentric_circle3,fill='lightblue')

#Texts

canvas.create_text([[175, 175]],text='prefs',font="arial 8")
canvas.create_text([[175-35, 175]],text='new',font="arial 8")
canvas.create_text([[175+35, 175]],text='scores',font="arial 8")
canvas.create_text( [[175, 150]],text='SIMÓN',font='Arial 23 bold')


#Diamonds(poligonos)

points_dia=[[-70, -10], [-150, -10], [-150, -60], [-60, -150], [-10, -150], [-10, -70], [-30, -70], [-70, -30]]
homogenize(points_dia)
colors=(('green4', 'green3'), ('cyan4', 'cyan3'), ('red4', 'red3'), ('yellow4', 'yellow3'))



trans=gettranslation(175,175)
contador = 0


for rot in range(0, 360,90):
    rotation=getrotation(rot)
    transform= np.dot(rotation,trans).tolist()
    temp = list()
    for i in range(len(points_dia)):
        temp.append(np.dot(points_dia[i],transform).tolist())

    dehomogenize(temp)
    dia1=canvas.create_polygon(temp,fill=colors[contador][0],activefill=colors[contador][1])
    canvas.tag_bind(dia1,"<Enter>",lambda e: incresure())

    contador+=1





#Label
window=[[175, 220]]
var = IntVar()
label_score= Label(canvas,relief='groove', background="black",textvariable = var, foreground="red",anchor='e')
canvas.create_window(window,width=60, height=20, window=label_score)

#funtions



def incresure():
    num = int(var.get())
    var.set(str(num + 10))


def reset():
    num = int(var.get())
    num = 0
    var.set(str(num))


canvas.tag_bind(smallest_concentric_circle1,"<Button-1>",lambda e: reset())





root.mainloop()