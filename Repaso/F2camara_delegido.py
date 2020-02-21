from tkinter import *
from tkinter import ttk
import numpy as np

class Simon(Canvas):


    def homogenize(self,coords: list):
        for i in range(len(coords)):
            coords[i].append(1)
        return coords

    def homogenize2(self, coords: list):
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

    def incresure(self):
        num = int(self.var.get())
        self.var.set(str(num + 10))

    def reset(self):
        self.var.set(0)



    def __init__(self, master=None, **options):
        super().__init__(master, options)
        self.w0 = 350
        self.h0 = 350

        self.lastneedle = None

        self.w = int(self.cget('width'))
        self.h = int(self.cget('height'))

        self.xscl = self.w / self.w0
        self.yscl = self.h / self.h0

        self.scale = self.getscaled(self.xscl, self.yscl)




        biggest_circle = [[5, 5], [345, 345]]
        self.homogenize(biggest_circle)
        biggest_circle=np.dot(biggest_circle,self.scale).tolist()
        self.dehomogenize(biggest_circle)
        self.create_oval(biggest_circle, fill='grey')


        medium_circle = [[10, 10], [340, 340]]
        self.homogenize(medium_circle)
        medium_circle=np.dot(medium_circle,self.scale).tolist()
        self.dehomogenize(medium_circle)
        self.create_oval(medium_circle, fill='black')


        smallest_circle = [[110, 110], [240, 240]]
        self.homogenize(smallest_circle)
        smallest_circle=np.dot(smallest_circle,self.scale).tolist()
        self.dehomogenize(smallest_circle)
        self.create_oval(smallest_circle, fill='silver')

    # Small_concentric_circles

        biggest_concentric_circle1 = [[165, 180], [185, 200]]
        self.homogenize(biggest_concentric_circle1)
        biggest_concentric_circle1=np.dot(biggest_concentric_circle1,self.scale).tolist()
        self.dehomogenize(biggest_concentric_circle1)
        self.create_oval(biggest_concentric_circle1, fill='black')


        smallest_concentric_circle1 = [[167, 182], [183, 198]]
        self.homogenize(smallest_concentric_circle1)
        smallest_concentric_circle1=np.dot(smallest_concentric_circle1,self.scale).tolist()
        self.dehomogenize(smallest_concentric_circle1)
        smallest_concentric_circle1=self.create_oval(smallest_concentric_circle1, fill='red')
        self.tag_bind(smallest_concentric_circle1, "<Button-1>", lambda e: self.reset())




        biggest_concentric_circle2 = [[165 - 35, 180], [185 - 35, 200]]
        self.homogenize(biggest_concentric_circle2)
        biggest_concentric_circle2=np.dot(biggest_concentric_circle2,self.scale).tolist()
        self.dehomogenize(biggest_concentric_circle2)
        self.create_oval(biggest_concentric_circle2, fill='black')



        smallest_concentric_circle2 = [[167 - 35, 182], [183 - 35, 198]]
        self.homogenize(smallest_concentric_circle2)
        smallest_concentric_circle2=np.dot(smallest_concentric_circle2,self.scale).tolist()
        self.dehomogenize(smallest_concentric_circle2)
        self.create_oval(smallest_concentric_circle2, fill='yellow')



        biggest_concentric_circle3 = [[165 + 35, 180], [185 + 35, 200]]
        self.homogenize(biggest_concentric_circle3)
        biggest_concentric_circle3 = np.dot(biggest_concentric_circle3, self.scale).tolist()
        self.dehomogenize(biggest_concentric_circle3)
        self.create_oval(biggest_concentric_circle3, fill='black')



        smallest_concentric_circle3 = [[167 + 35, 182], [183 + 35, 198]]
        self.homogenize(smallest_concentric_circle3)
        smallest_concentric_circle3=np.dot(smallest_concentric_circle3,self.scale).tolist()
        self.dehomogenize(smallest_concentric_circle3)
        self.create_oval(smallest_concentric_circle3, fill='lightblue')

    # Texts
        texto1=[[175, 175]]
        self.homogenize(texto1)
        sca=np.dot(texto1,self.scale).tolist()
        self.dehomogenize(sca)
        self.create_text(sca, text='prefs', font="arial 8")





        texto2 = [[175 - 35, 175]]
        self.homogenize(texto2)
        sca = np.dot(texto2, self.scale).tolist()
        self.dehomogenize(sca)
        self.create_text(sca, text='new', font="arial 8")





        texto3=[[175 + 35, 175]]
        self.homogenize(texto3)
        sca = np.dot(texto3, self.scale).tolist()
        self.dehomogenize(sca)
        self.create_text(sca,text='scores', font="arial 8")




        texto4=[[175, 150]]
        self.homogenize(texto4)
        sca = np.dot(texto4,self.scale).tolist()
        self.dehomogenize(sca)
        self.create_text(sca, text='SIMÓN', font='Arial 23 bold')

    # Diamonds(poligonos)

        points_dia = [[-70, -10], [-150, -10], [-150, -60], [-60, -150], [-10, -150], [-10, -70], [-30, -70], [-70, -30]]
        self.homogenize(points_dia)
        colors = (('green4', 'green3'), ('cyan4', 'cyan3'), ('red4', 'red3'), ('yellow4', 'yellow3'))

        trans = self.gettranslation(175, 175)
        contador = 0

        for rot in range(0, 360, 90):
            rotation = self.getrotation(rot)
            transform = np.dot(rotation, trans).tolist()
            temp = list()
            for i in range(len(points_dia)):
                temp.append(np.dot(points_dia[i], transform).tolist())
                sca = np.dot(temp,self.scale).tolist()
                self.dehomogenize(sca)
            self.dehomogenize(temp)
            dia1 = self.create_polygon(sca, fill=colors[contador][0], activefill=colors[contador][1])
            self.tag_bind(dia1, "<Enter>", lambda e: self.incresure())

            contador += 1

        # Label
        window = [[175, 220]]
        self.homogenize(window)
        sca = np.dot(window,self.scale).tolist()
        self.dehomogenize(sca)
        self.var = IntVar()
        label_score = Label(self, relief='groove', background="black", textvariable=self.var, foreground="red", anchor='e')
        self.create_window(sca, width=60, height=20, window=label_score)

    # funtions

