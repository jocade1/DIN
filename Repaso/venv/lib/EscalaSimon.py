from tkinter import *
from tkinter import ttk
import numpy as np


class SimonEscalada(Canvas):
    def homogenize(self, coords: list):
        for i in range(len(coords)):
            coords[i].append(1)

    def dehomogenize(self, coords: list):
        for i in range(len(coords)):
            coords[i][0] = coords[i][0] / coords[i][2]
            coords[i][1] = coords[i][1] / coords[i][2]
            del coords[i][2]

    def gettranslation(self, tx: float, ty: float) -> list:
        return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]

    def getrotation(self, deg: float) -> list:
        rad = np.radians(deg)
        return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]

    def getscaled(self, xscl:float, yscl:float) -> list:
        return [[xscl, 0, 0], [0, yscl, 0], [0, 0, 1]]



    def __init__(self, master=None, **options):
        super().__init__(master, options)
        self.w0 = 400
        self.h0 = 400

        self.lastneedle = None

        self.w = int(self.cget('width'))
        self.h = int(self.cget('height'))

        self.xscl = self.w / self.w0
        self.yscl = self.h / self.h0

        self.scale = self.getscaled(self.xscl, self.yscl)

        cir1=[[10,10,],[390,390]]
        self.homogenize(cir1)
        cir1=np.dot(cir1,self.scale).tolist()
        self.dehomogenize(cir1)
        self.create_oval(cir1 ,fill='grey')

        c2=[[20,20,],[380,380]]
        self.homogenize(c2)
        c2=np.dot(c2,self.scale).tolist()
        self.dehomogenize(c2)
        self.create_oval(c2,fill='black')

        c3 = [[120, 120, ], [280, 280]]
        self.homogenize(c3)
        c3 = np.dot(c3, self.scale).tolist()
        self.dehomogenize(c3)
        self.create_oval(c3, fill='grey')

        #texto

        simon=[[195, 160]]
        self.homogenize(simon)
        s=np.dot(simon,self.scale).tolist()
        self.dehomogenize(s)
        self.create_text(s,text='SIMON',font="arial 20")

        simon = [[140, 210]]
        self.homogenize(simon)
        s = np.dot(simon, self.scale).tolist()
        self.dehomogenize(s)
        self.create_text(s, text='New', font="arial 12")

        simon = [[200,210]]
        self.homogenize(simon)
        s = np.dot(simon, self.scale).tolist()
        self.dehomogenize(s)
        self.create_text(s, text='Prets', font="arial 12")

        simon = [[250,210]]
        self.homogenize(simon)
        s = np.dot(simon, self.scale).tolist()
        self.dehomogenize(s)
        self.create_text(s, text='Score', font="arial 12")

        #circulos pequeños

        c4 = [[135, 220, ], [165, 250]]
        self.homogenize(c4)
        c4 = np.dot(c4, self.scale).tolist()
        self.dehomogenize(c4)
        self.create_oval(c4, fill='black')

        c5 = [[185, 220, ], [215, 250]]
        self.homogenize(c5)
        c5 = np.dot(c5, self.scale).tolist()
        self.dehomogenize(c5)
        self.create_oval(c5, fill='black')


        c6 = [[235, 220, ], [265, 250]]
        self.homogenize(c6)
        c6 = np.dot(c6, self.scale).tolist()
        self.dehomogenize(c6)
        self.create_oval(c6, fill='black')

        c7 = [[137, 222, ], [163, 248]]
        self.homogenize(c7)
        c7 = np.dot(c7, self.scale).tolist()
        self.dehomogenize(c7)
        c7=self.create_oval(c7, fill='yellow')

        c8 = [[187, 222, ], [213, 248]]
        self.homogenize(c8)
        c8 = np.dot(c8, self.scale).tolist()
        self.dehomogenize(c8)
        self.create_oval(c8, fill='red')

        c9 = [[237, 222, ], [263, 248]]
        self.homogenize(c9)
        c9 = np.dot(c9, self.scale).tolist()
        self.dehomogenize(c9)
        self.create_oval(c9, fill='blue')

        var = IntVar()
        ##Entry
        en = Entry(self, width=int(self.w / 100), bg="black", textvariable=var, fg="red")
        p=[[185,254]]
        self.homogenize(p)
        p = np.dot(p, self.scale).tolist()
        self.dehomogenize(p)
        en.place(x=p[0][0], y=p[0][1])

        #Poligonos

        pol = [[-160.0, -10.0], [-90.0, -10.0], [-90.0, -30.0], [-30.0, -90.0], [-10.0, -90.0], [-10.0, -160.0],
               [-65.0, -160.0], [-160.0, -65.0]]
        self.homogenize(pol)
        toorig = self.gettranslation(200, 200)
        rotation = self.getrotation(0)
        transform = np.dot(rotation, toorig)
        needle2 = np.dot(pol, transform)
        needle2 = np.dot(needle2, self.scale).tolist()
        self.dehomogenize(needle2)
        pol1=self.create_polygon(needle2,  fill='green',activefill="lightgreen")


        toorig = self.gettranslation(200, 200)
        rotation = self.getrotation(90)
        transform = np.dot(rotation, toorig)
        needle3 = np.dot(pol, transform)
        needle3 = np.dot(needle3, self.scale).tolist()
        self.dehomogenize(needle3)
        pol2= self.create_polygon(needle3, fill='blue',activefill="lightblue")

        toorig = self.gettranslation(200, 200)
        rotation = self.getrotation(180)
        transform = np.dot(rotation, toorig)
        needle3 = np.dot(pol, transform)
        needle3 = np.dot(needle3, self.scale).tolist()
        self.dehomogenize(needle3)
        pol3 = self.create_polygon(needle3, fill='red',activefill="pink")

        toorig = self.gettranslation(200, 200)
        rotation = self.getrotation(270)
        transform = np.dot(rotation, toorig)
        needle3 = np.dot(pol, transform)
        needle3 = np.dot(needle3, self.scale).tolist()
        self.dehomogenize(needle3)
        pol4 = self.create_polygon(needle3, fill='yellow',activefill="lightyellow")

        def sumar():
            numero = int(var.get())
            var.set(str(numero + 10))

        def start():
            numero = int(var.get())
            numero = 0
            var.set(str(numero))

        self.tag_bind(c7, "<Button-1>", lambda e: start())
        self.tag_bind(pol1, "<Enter>", lambda e:sumar())
        self.tag_bind(pol2, "<Enter>", lambda e: sumar())
        self.tag_bind(pol3, "<Enter>", lambda e: sumar())
        self.tag_bind(pol4, "<Enter>", lambda e: sumar())