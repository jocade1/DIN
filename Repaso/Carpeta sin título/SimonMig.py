from tkinter import *
from tkinter import ttk
import numpy as np

class Simon(Canvas):


    def homogenize(self, coords: list):
        for i in range(len(coords)):
            coords[i].append(1)
        return coords

    def homogenize2(self,coords: list):
        for i in range(len(coords)):
            coords[i].append(1)

    def dehomogenize(self,coords: list):
        for i in range(len(coords)):
            coords[i][0] = coords[i][0] / coords[i][2]
            coords[i][1] = coords[i][1] / coords[i][2]
            del coords[i][2]

    def gettranslation(self,tx: float, ty: float) -> list:
        return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]


    def getscaled(self, xscl:float, yscl:float) -> list:
        return [[xscl, 0, 0], [0, yscl, 0], [0, 0, 1]]

    def getrotation(self,deg: float) -> list:
        rad = np.radians(deg)
        return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]


    def __init__(self, master=None, **options):
        super().__init__(master, options)
        self.w0 = 400
        self.h0 = 400



        self.w = int(self.cget('width'))
        self.h = int(self.cget('height'))

        self.xscl = self.w / self.w0
        self.yscl = self.h / self.h0

        self.scale = self.getscaled(self.xscl, self.yscl)


        c1 = [[10, 10, ], [390, 390]]
        self.homogenize(c1)
        pointsC1 = np.dot(c1,self.scale).tolist()
        self.dehomogenize(pointsC1)
        self.create_oval(pointsC1, fill='grey')

        c2 = [[20, 20, ], [380, 380]]
        self.homogenize(c2)
        pointsC2 = np.dot(c2,self.scale).tolist()
        self.dehomogenize(pointsC2)
        self.create_oval(pointsC2, fill='black')

        c3 = [[120, 120, ], [280, 280]]
        self.homogenize(c3)
        pointsC3 = np.dot(c3, self.scale).tolist()
        self.dehomogenize(pointsC3)
        self.create_oval(pointsC3, fill='grey')

        ##texto
        text1=[[195, 160]]
        self.homogenize(text1)
        pointstext1 = np.dot(text1,self.scale).tolist()
        self.dehomogenize(pointstext1)


        self.create_text(pointstext1, text='SIMON')
        self.create_text([[140, 210]], text='New')
        self.create_text([[200, 210]], text='Prets')
        self.create_text([[250, 210]], text='Score')

        # circulos
        c4 = [[135, 220, ], [165, 250]]
        self.homogenize(c4)
        pointsC4 = np.dot(c4, self.scale).tolist()
        self.dehomogenize(pointsC4)
        self.create_oval(pointsC4, fill='black')



        c5 = [[185, 220, ], [215, 250]]
        self.homogenize(c5)
        pointsC5 = np.dot(c5, self.scale).tolist()
        self.dehomogenize(pointsC5)
        self.create_oval(pointsC5, fill='black')




        c6 = [[235, 220, ], [265, 250]]
        self.homogenize(c6)
        pointsC6 = np.dot(c6, self.scale).tolist()
        self.dehomogenize(pointsC6)
        self.create_oval(pointsC6, fill='black')




        c7 = [[137, 222, ], [163, 248]]
        self.homogenize(c7)
        pointsC7 = np.dot(c7, self.scale).tolist()
        self.dehomogenize(pointsC7)
        c7 = self.create_oval(pointsC7, fill='yellow')



        c8 = [[187, 222, ], [213, 248]]
        self.homogenize(c8)
        pointsC8 = np.dot(c8, self.scale).tolist()
        self.dehomogenize(pointsC8)
        self.create_oval(pointsC8, fill='red')




        c9 = [[237, 222, ], [263, 248]]
        self.homogenize(c9)
        pointsC9 = np.dot(c9, self.scale).tolist()
        self.dehomogenize(pointsC9)
        self.create_oval(pointsC9, fill='blue')

        var = IntVar()
        ##Entry
        en = Entry(master, width=int(self.w0/ 100), bg="black", textvariable=var, fg="red")
        en.place(x=185, y=254)


        #poligonos


        pol = [[-160.0, -10.0], [-90.0, -10.0], [-90.0, -30.0], [-30.0, -90.0], [-10.0, -90.0], [-10.0, -160.0],
               [-65.0, -160.0], [-160.0, -65.0]]
        self.homogenize(pol)
        pointspol= np.dot(pol,self.scale).tolist()
        self.dehomogenize(pointspol)





        poligono2 = [[-160.0, -10.0], [-90.0, -10.0], [-90.0, -30.0], [-30.0, -90.0], [-10.0, -90.0], [-10.0, -160.0],[-65.0, -160.0], [-160.0, -65.0]]

        self.homogenize(poligono2)
        f = self.gettranslation(200, 200)

        rotation = self.getrotation(0)
        transform = np.dot(rotation, f)
        poligono2 = (np.dot(pol, transform).tolist())

        self.dehomogenize(poligono2)
        p1 = self.create_polygon(poligono2, fill="green", activefill="lightgreen")

        po3 = [[-160.0, -10.0], [-90.0, -10.0], [-90.0, -30.0], [-30.0, -90.0], [-10.0, -90.0], [-10.0, -160.0],
               [-65.0, -160.0], [-160.0, -65.0]]
        f = self.gettranslation(200, 200)
        rotation = self.getrotation(90)
        transform = np.dot(rotation, f)
        pol3 = (np.dot(pol, transform).tolist())
        self.dehomogenize(pol3)
        p2 = self.create_polygon(pol3, fill="blue", activefill="lightblue")

        po3 = [[-160.0, -10.0], [-90.0, -10.0], [-90.0, -30.0], [-30.0, -90.0], [-10.0, -90.0], [-10.0, -160.0],
               [-65.0, -160.0], [-160.0, -65.0]]
        f = self.gettranslation(200, 200)
        rotation = self.getrotation(180)
        transform = np.dot(rotation, f)
        pol3 = (np.dot(pol, transform).tolist())
        self.dehomogenize(pol3)
        p3 = self.create_polygon(pol3, fill="red", activefill="pink")




        po3 = [[-160.0, -10.0], [-90.0, -10.0], [-90.0, -30.0], [-30.0, -90.0], [-10.0, -90.0], [-10.0, -160.0],
               [-65.0, -160.0], [-160.0, -65.0]]
        f = self.gettranslation(200, 200)
        rotation = self.getrotation(270)
        transform = np.dot(rotation, f)
        pol3 = (np.dot(pol, transform).tolist())
        self.dehomogenize(pol3)
        p4 = self.create_polygon(pol3, fill="yellow", activefill="lightyellow")

        def sumar():
            numero = int(var.get())
            var.set(str(numero + 10))

        def zero():
            numero = int(var.get())
            numero = 0
            var.set(str(numero))

        self.bind('<Button-3>', lambda e: print(e.x, e.y))
        self.tag_bind(c7, "<Button-1>", lambda e: zero())
        self.tag_bind(p1, "<Enter>", lambda e: sumar())
        self.tag_bind(p2, "<Enter>", lambda e: sumar())
        self.tag_bind(p3, "<Enter>", lambda e: sumar())
        self.tag_bind(p4, "<Enter>", lambda e: sumar())



