from tkinter import *
from tkinter import ttk
from childw import newWindow


#def des(new):
 #   if messagebox.askyesno(message="¿Estás seguro de querer salir?",icon='question',title='Salir'):
  #      new.destroy()

root=Tk()
ttk.Button(root,text="New window").pack()
ttk.Button(root,text="Minimize",command=lambda :root.iconify()).pack()
root.geometry("300x200-5+40")
root.minsize(200,100)
root.maxsize(500,500)
root.update()

root.option_add('*tearOff', FALSE)#evita que se salga el menu, se pone antes del menu
menubar = Menu(root)
menu_nuevo = Menu(menubar)
root['menu'] = menubar #Sin esto no sale
menubar.add_command(label='New',command=lambda :newWindow(root))
menu_button=Menu(menubar)
menubar.add_cascade(menu=menu_button,label="Buttons")
check=StringVar()
menu_button.add_checkbutton(label="Check", variable=check, onvalue=1, offvalue=0)
menu_button.add_separator()#separador
radio=StringVar()
menu_button.add_radiobutton(label="Radio1",variable=radio,value=1)
menu_button.add_radiobutton(label="Radio2",variable=radio,value=2)
root.option_add('*tearOff', FALSE)
menu=Menu(root)
for i in ('One', 'Two', 'Three'):
    menu.add_command(label=i)
if (root.tk.call('tk', 'windowingsystem')=='aqua'):
    root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
    root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
else:
    root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))
popmenu=Menu(root)





root.mainloop()