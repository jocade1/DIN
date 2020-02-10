import tkinter
import math

window = tkinter.Tk()
window.title("Calculadora")
window.geometry("392x488")
label = tkinter.Entry(window,font=("arial",20,"bold"),width =22).place(x=10, y =60)


#Botones
Boton0 = tkinter.Button(window,text="0").place(x=198 ,y=288)
Boton1 = tkinter.Button(window,text="1").place(x=21 ,y=276)
Boton2 = tkinter.Button(window,text="2").place(x=80,y=276)
Boton3 = tkinter.Button(window,text="3").place(x=139,y=276)
Boton4 = tkinter.Button(window,text="4").place(x=21,y=228)
Boton5 = tkinter.Button(window,text="5").place(x=80,y=228)
Boton6 = tkinter.Button(window,text="6").place(x=139,y=228)
Boton7 = tkinter.Button(window,text="7").place(x=21,y=180)
Boton8 = tkinter.Button(window,text="8").place(x=80,y=180)
Boton9 = tkinter.Button(window,text="9").place(x=139,y=180)
#BotonSuma = tkinter.Button(window,text="+").place(x=,y=)
#BotonResta = tkinter.Button(window,text="-").place(x=,y=)
BotonDivide = tkinter.Button(window,text="/").place(x=198,y=180)
BotonMultiplica = tkinter.Button(window,text="*").place(x=257,y=228)
#BotonIgual = tkinter.Button(window,text="=").place(x=,y=)
#BotonComa = tkinter.Button(window,text=".").place(x=,y=)
#BotonMc = tkinter.Button(window,text="Mc").place(x=257,y=)
BotonMs = tkinter.Button(window,text="Ms").place(x=257,y=180)
#BotonMr = tkinter.Button(window,text="Mr").place(x=257,y)
#BotonBorrar= tkinter.Button(window,text="Del").place(x=257,y=)
 








window.mainloop()