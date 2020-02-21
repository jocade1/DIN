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

def sumar():
    numero=int(var.get())
    var.set(str(numero+10))

def zero():
    numero = int(var.get())
    numero=0
    var.set(str(numero))




ventana=Tk()
ventana.title("SIMON")
frame=Frame(ventana)
frame.pack()
w=400
h=400
canvas=Canvas(frame,widt=w, height=h)
canvas.grid(row=0, column=0)

c1=[[10,10,],[390,390]]
canvas.create_oval(c1,fill='grey')

c2=[[20,20,],[380,380]]
canvas.create_oval(c2,fill='black')

c3=[[120,120,],[280,280]]
canvas.create_oval(c3,fill='grey')

##texto
canvas.create_text([[195,160]],text='SIMÓN',font="arial 20")
canvas.create_text([[140,210]],text='New')
canvas.create_text([[200,210]],text='Prets')
canvas.create_text([[250,210]],text='Score')

#circulos
c4=[[135,220,],[165,250]]
canvas.create_oval(c4,fill='black')
c5=[[185,220,],[215,250]]
canvas.create_oval(c5,fill='black')
c6=[[235,220,],[265,250]]
canvas.create_oval(c6,fill='black')

c7=[[137,222,],[163,248]]
c7=canvas.create_oval(c7,fill='yellow')
c8=[[187,222,],[213,248]]
canvas.create_oval(c8,fill='pink')
c9=[[237,222,],[263,248]]
canvas.create_oval(c9,fill='blue')

var=IntVar()
##Entry
en=Entry(ventana,width=int(w/100),bg="black",textvariable=var,fg="red")
en.place(x=185,y=254)


##poligono

pol=[[-160.0, -10.0], [-90.0, -10.0], [-90.0, -30.0], [-30.0, -90.0], [-10.0, -90.0], [-10.0, -160.0], [-65.0, -160.0], [-160.0, -65.0]]
homogenize(pol)

po2=list()
f=gettranslation(200,200)
rotation = getrotation(0)
transform = np.dot(rotation, f)

pol2=(np.dot(pol, transform).tolist())
dehomogenize(pol2)
p1=canvas.create_polygon(pol2,fill="green",activefill="lightgreen")

po3 = list()
f = gettranslation(200, 200)
rotation = getrotation(90)
transform = np.dot(rotation, f)
pol3 = (np.dot(pol, transform).tolist())
dehomogenize(pol3)
p2=canvas.create_polygon(pol3, fill="blue",activefill="lightblue")

po3 = list()
f = gettranslation(200, 200)
rotation = getrotation(180)
transform = np.dot(rotation, f)
pol3 = (np.dot(pol, transform).tolist())
dehomogenize(pol3)
p3=canvas.create_polygon(pol3, fill="red",activefill="pink")

po3 = list()
f = gettranslation(200, 200)
rotation = getrotation(270)
transform = np.dot(rotation, f)
pol3 = (np.dot(pol, transform).tolist())
dehomogenize(pol3)
p4=canvas.create_polygon(pol3, fill="yellow",activefill="lightyellow")




canvas.bind('<Button-3>',lambda e:print(e.x,e.y))
canvas.tag_bind(c7,"<Button-1>",lambda e:zero())
canvas.tag_bind(p1,"<Enter>",lambda e:sumar())
canvas.tag_bind(p2,"<Enter>",lambda e:sumar())
canvas.tag_bind(p3,"<Enter>",lambda e:sumar())
canvas.tag_bind(p4,"<Enter>",lambda e:sumar())

ventana.mainloop()