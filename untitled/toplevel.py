from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

root = Tk()

#def des(new):
 #   if messagebox.askyesno(message="are you sure you want to Exit?", icon='question', title='Exit'):
  #      new.destroy()


def newWindow():
    def closew():
        if messagebox.askyesno(message="are you sure you want to Exit?", icon='question', title='Exit'):
            new.destroy()

    new = Toplevel(root)
    var = StringVar()
    var.set('2')
    R1 = ttk.Radiobutton(new, text="Option 1",variable = var, value = '1')
    R1.pack()
    R2 = ttk.Radiobutton(new, text="Option 2",variable = var, value = '2')
    R2.pack()
    R3 = ttk.Radiobutton(new, text="Option 2",variable = var, value ='3')
    R3.pack()
    new.geometry("150x400")
    ttk.Button(new,text="Exit" ,command = lambda: closew()).pack()



buttonPage = ttk.Button(root, text = "New windows")
ttk.Button(root, text ="minimize ", command = lambda: root.iconify()).pack()
buttonPage.pack()
root.geometry("320x211")
root.minsize(200,100)
root.maxsize(500,500)
def saved():
    filename = filedialog.askopenfilename()
    filename = filedialog.asksaveasfilename()
    dirname = filedialog.askdirectory()


memubar =  Menu(root)
menu_nuevo = Menu(memubar)

root['menu'] = memubar


memubar.add_command(label='New', command=lambda  :newWindow())

root.mainloop()