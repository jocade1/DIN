from tkinter import ttk

window = ttk.tkinter.Tk()

frame = ttk.Frame(window, borderwidth=15, relief="ridge")
frame.pack(fill="both", expand=1)

labels = []

label00= ttk.Label(frame, relief="ridge")
label00.grid(row=0, column=0, sticky="nswe")
labels.append(label00)

label01 = ttk.Label(frame, relief="ridge")
label01.grid(row=0, column=1, sticky="nswe")
labels.append(label01)


label02 = ttk.Label(frame, relief="ridge")
label02.grid(row=0, column=2, sticky="nswe")
labels.append(label02)


label03 = ttk.Label(frame, relief="ridge")
label03.grid(row=0, column=3, sticky="nswe")
labels.append(label03)


label10 = ttk.Label(frame, relief="ridge")
label10.grid(row=1, column=0, sticky="nswe")
labels.append(label10)

label11 = ttk.Label(frame, relief="ridge")
label11.grid(row=1, column=1, sticky="nswe")
labels.append(label11)

label10 = ttk.Label(frame, relief="ridge")
label10.grid(row=1, column=2, sticky="nswe")
labels.append(label10)

label13 = ttk.Label(frame, relief="ridge")
label13.grid(row=1, column=3, sticky="nswe")
labels.append(label13)



label20 = ttk.Label(frame, relief="ridge")
label20.grid(row=2, column=0, sticky="nswe")
labels.append(label20)


label21 = ttk.Label(frame, relief="ridge")
label21.grid(row=2, column=1, sticky="nswe")
labels.append(label21)

label22 = ttk.Label(frame, relief="ridge")
label22.grid(row=2, column=2, sticky="nswe")
labels.append(label22)


label23 = ttk.Label(frame, relief="ridge")
label23.grid(row=2, column=3, sticky="nswe")
labels.append(label23)


label30 = ttk.Label(frame, relief="ridge")
label30.grid(row=3, column=0, sticky="nswe")
labels.append(label30)


label31 = ttk.Label(frame, relief="ridge")
label31.grid(row=3, column=1, sticky="nswe")
labels.append(label31)

label32 = ttk.Label(frame, relief="ridge")
label32.grid(row=3, column=2, sticky="nswe")
labels.append(label32)


label33 = ttk.Label(frame, relief="ridge")
label33.grid(row=3, column=3, sticky="nswe")
labels.append(label33)


frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
window.mainloop()
