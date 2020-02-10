import tkinter
from tkinter.font import Font

def changeFont(entry:tkinter.Entry, bold, corsiva, underline):
    myfont = Font(weight='bold' if bold.get() else 'normal',
                  slant='italic' if corsiva.get() else 'roman',
                  underline = underline.get())
    entry.configure(font=myfont)



window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
entry = tkinter.Entry(frame)
entry.pack(side='left')
frame2 = tkinter.Frame(window)
frame2.pack()
bold = tkinter.IntVar()
corsiva = tkinter.IntVar()
underline = tkinter.IntVar()
boldCheck = tkinter.Checkbutton(frame2, text='Bold', variable=bold)
boldCheck.pack(side='left')
corsivaCheck = tkinter.Checkbutton(frame2, text='Cursiva', variable=corsiva)
corsivaCheck.pack(side='left')
underCheck = tkinter.Checkbutton(frame2, text='Underline', variable=underline)
underCheck.pack(side='left')
button = tkinter.Button(frame2, text='update', command=lambda: changeFont(entry,bold,corsiva,underline))
button.pack()

window.mainloop()