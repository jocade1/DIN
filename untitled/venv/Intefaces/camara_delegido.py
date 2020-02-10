from tkinter import *
def change(widget, colors):
    new_val = '#'
    for name in ('red', 'green', 'blue'):
        new_val += colors[name].get()
    widget['bg'] = new_val
    widget['anchor'] = 'S'



window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
window.geometry("300x110")
window.resizable(0,0)
labelRed = tkinter.Label(window,text="Red",font='Helvetica' ,width =5).place(x=35,y=2)
labelGreen = tkinter.Label(window,text="Green",font='Helvetica' , width = 5).place(x=30, y=20)
labelBlue = tkinter.Label(window, text="Blue", font='Helvetica' , width = 5).place(x=32,y=40)
buttonPlusRed = tkinter.Button(window,text="+").place(x=192 ,y=-3)
buttonPlusGreen =tkinter.Button(window,text="+").place(x=192 ,y=20)
buttonPlusBlue =tkinter.Button(window,text="+").place(x=192 ,y=40)
buttonMenosRed = tkinter.Button(window,text="-").place(x=76 ,y=-3)
buttonMenosGreen =tkinter.Button(window,text="-").place(x=76 ,y=20)
buttonMenosBlue =tkinter.Button(window,text="-").place(x=76 ,y=40)

colors = {}
for (name, col) in (('red', '#FF0000'),('green', '#00FF00'),('blue', '#0000FF')):
    colors[name] = tkinter.StringVar()
    colors[name].set('255')
    entry = tkinter.Entry(frame, textvariable=colors[name], bg=col,fg='white',width= 10)
    entry.pack()




mix = tkinter.Button(window,text= "Mix",font='Helvetica',bg= 'White',height=3).place(x=230,y=-4)

tkinter.mainloop()