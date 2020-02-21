from tkinter import *
from tkinter import ttk
import numpy as np
class SimonClass(Canvas):

    def xy(self,event):
        global lastx, lasty
        lastx, lasty = self.canvasx(event.x), self.canvasy(event.y)

    def homogenize(self,coords: list):
        for i in range(len(coords)):
            coords[i].append(1)

    def dehomogenize(self,coords: list):
        for i in range(len(coords)):
            coords[i][0] = coords[i][0] / coords[i][2]
            coords[i][1] = coords[i][1] / coords[i][2]
            del coords[i][2]

    def gettranslation(self,tx: float, ty: float) -> list:
        return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]

    def getrotation(self,deg: float) -> list:
        rad = np.radians(deg)
        return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]

    # Lo usa en una clase a parte donde lo llama desde ahi
    def getscaled(self, xscl: float, yscl: float) -> list:
        return [[xscl, 0, 0], [0, yscl, 0], [0, 0, 1]]

    def point(self,num:int):
        num=0


    def __init__(self, master=None, **options):
        super().__init__(master, options)
        self.w0=600
        self.h0=600

        self.w = int(self.cget('width'))
        self.h = int(self.cget('height'))

        self.xscl = self.w / self.w0
        self.yscl = self.h / self.h0

        self.scale = self.getscaled(self.xscl, self.yscl)
