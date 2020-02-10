from tkinter import messagebox
from tkinter import *
from tkinter import ttk


def newWindow(window:Tk):

    new=Toplevel(window)
    lf=ttk.Labelframe(new,text="Frame")
    lf.pack()
    style = ttk.Style()#Si se encuentra fuera crea una ventana a parte sin nada
    var=StringVar()
    var.set(style.theme_use())#Pone el radiobutton por defecto

    for t in style.theme_names():
        ttk.Radiobutton(lf,text=t,variable=var,value=t,command=lambda : style.theme_use(var.get())).pack(anchor='w')#Coge para cada radiobutton un style diferente
        #command=lambda x=t : s.theme_use(x) se puede poner asi tambien


    button=ttk.Button(lf,text="Destroy",command=lambda :close())
    button.pack()
    new.update()
    new.minsize(300,200)
    new.maxsize(400,500)
    n=IntVar(0)
    Spinbox(lf,from_=0,to=100,textvariable=n).pack()
    ttk.Progressbar(lf,orient=HORIZONTAL,length=200,mode='determinate',variable=n).pack()
    def close():
        if messagebox.askyesno(message="¿Estás seguro de querer salir?", icon='question', title='Salir'):
            new.destroy()






