from tkinter import *
from tkinter import ttk

window = Tk()

#Button
statebuttons = StringVar()

#CheckButton
statecheckbuttons = StringVar()
measureSystem=StringVar()

#RadioButton
phone = StringVar()
rd1 =StringVar()
rd2 =StringVar()
rd3 =StringVar()

#ComboBox
contryvar=StringVar()
labelvar=StringVar()

def refresh():
    statebuttons.set(button.state())
    statecheckbuttons.set(check.state())
    rd1.set(home.state())
    rd2.set(office.state())
    rd3.set(cell.state())
    labelvar.set(combobox.state())

frame = ttk.Frame(window)
frame.grid(column=0,row=0)
label = ttk.Label(frame,textvar=statebuttons)
label.grid(column = 0,row =0)
button=ttk.Button(frame,text="Click")
button.grid(column = 1,row =0)

check = ttk.Checkbutton(frame,variable=measureSystem,onvalue="ON",offvalue="OFF")
check.grid(column = 0,row =1)

labelcheck=ttk.Label(frame,text="Status CheckButton",textvar=statecheckbuttons)
labelcheck.grid(column=1,row=1)

home = ttk.Radiobutton(frame,text="Home",variable=phone,value='home')
home.grid(column=0,row=2)
labelhome=ttk.Label(frame,text="Home",textvar=rd1)
labelhome.grid(column=1,row=2)

office = ttk.Radiobutton(frame,text='Office',variable=phone, value='office')
office.grid(column=1,row=1)
labeloffice=ttk.Label(frame,text="Office",textvar=rd2)
labeloffice.grid(column=1,row=3)

cell=ttk.Radiobutton(frame, text='Mobile', variable = phone, value='cell')
cell.grid(column=0,row=4)
labelcell=ttk.Label(frame,text="cell", textvariable=rd3)
labelcell.grid(column =1,row=4)

combobox=ttk.Label(frame,textvariable=contryvar)
combobox.grid(column=0,row=5)
combobox["values"] = {'USA', 'Canada', 'Australia'}
combobox.state("readonly")
labelCombobox=ttk.Label(frame,textvariable= labelvar)
labelCombobox.grid(column=1,row=5)

window.bind('<Return>', lambda e:refresh())

window.mainloop()