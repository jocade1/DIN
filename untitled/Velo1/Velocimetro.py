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
f = ttk.Frame()
f.pack()

spd = Canvas(f, width=400, height=400)
spd.grid(row=0, column=0)

spd.create_oval(15,15,385,385,fill='grey')
spd.create_oval(20,20,380,380,fill='white')

spd.create_oval(175,175,225,225,fill='grey')
spd.create_oval(180,180,220,220,fill='black')

spd.create_text([[200, 235]], text='km/h')
spd.create_oval(90,275,95,280, fill='black')


short = [[-175, 0],[-150, 0]]
homogenize(short)
toorig = gettranslation(200, 200)
for rot in range(-20,220,20):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = np.dot(short,transform).tolist()
    dehomogenize(temp)
    spd.create_line(temp)

large = [[-175, 0],[-140, 0]]
homogenize(large)
toorig = gettranslation(200, 200)
for rot in range(-30,220,20):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = np.dot(large,transform).tolist()
    # for i in range(len(short)):
    #     temp.append(np.dot(large[i],transform).tolist())
    dehomogenize(temp)
    spd.create_line(temp)

pos = [[-120, 0]]
homogenize(pos)
toorig = gettranslation(200, 200)
vel = 0
for rot in range(-30,220,20):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = np.dot(pos,transform).tolist()
    # temp.append(np.dot(pos[0],transform).tolist())
    dehomogenize(temp)
    spd.create_text(temp, text=str(vel))
    vel = vel + 20


needle = [[0,0], [-7, -7], [0, -150], [7, -7]]
homogenize(needle)
toorig = gettranslation(200, 200)
rotation = getrotation(-123)
transform = np.dot(rotation, toorig)
needle2 = np.dot(needle,transform).tolist()
# for i in range(len(needle)):
#     needle2.append(np.dot(needle[i],toorig).tolist())
dehomogenize(needle2)
spd.create_polygon(needle2, outline='#f11', fill='#1f1', width=2)


# topos = gettranslation(120, 50)
# rotation = getrotation(180)
# transform = np.dot(toorig, rotation)
# transform = np.dot(transform, topos)

# for i in range(len(triangle)):
#     triangle2.append(np.dot(triangle[i],transform).tolist())
# dehomogenize(triangle2)
#
# cnv.create_polygon(triangle2, outline='#f11', fill='#1f1', width=2)
#
#


root.mainloop()