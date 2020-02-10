from tkinter import *
from tkinter import ttk

class DragManager():
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="cross")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        pass

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        try:
            target['background'] = event.widget['background']
            event.widget['background'] = ''
        except:
            pass

root = Tk()
root.title("Grid Colors")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root,relief='raised')
mainframe.columnconfigure(0, weight=0)
mainframe.rowconfigure(0, weight=0)
mainframe.rowconfigure(5, weight=0)
for i in range(1,5):
    mainframe.columnconfigure(i, weight=1, minsize='35p')
    mainframe.rowconfigure(i, weight=1, minsize='35p')
mainframe.grid(column=0, row=0, sticky='nwse')

h_ckbx_str_array = list()
v_ckbx_str_array = list()
for i in range(4):
    h_ckbx_str_array.append(StringVar())
    v_ckbx_str_array.append(StringVar())
    aux_chk = ttk.Checkbutton(mainframe, variable=h_ckbx_str_array[i])
    aux_chk.grid(row=0, column=i+1)
    aux_chk = ttk.Checkbutton(mainframe, variable=v_ckbx_str_array[i])
    aux_chk.grid(row=i+1, column=0)
    h_ckbx_str_array[i].set('0')
    v_ckbx_str_array[i].set('0')

dnd = DragManager()
lblgrid = list()
for r in range(4):
    lblgrid.append([])
    for c in range(4):
        lblgrid[r].append(ttk.Label(mainframe, relief='groove'))
        lblgrid[r][c].grid(row=r+1, column=c+1, sticky='nwse')
        dnd.add_dragable(lblgrid[r][c])


cbbx_str = StringVar()
cbbx_color = ttk.Combobox(mainframe, textvariable=cbbx_str)
cbbx_color.grid(column=1, row=5, columnspan=4, sticky='nwse')
cbbx_color['values'] = ('black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta')
cbbx_str.set(cbbx_color['values'][0])
cbbx_color.bind('<<ComboboxSelected>>', lambda e: set_lbls_color(h_ckbx_str_array, v_ckbx_str_array, cbbx_color, lblgrid))

def get_coordinates(h:list, v:list)->list:
    coords = []
    for r in range(4):
        if v[r].get() == '1':
            for c in range(4):
                if h[c].get() == '1':
                    coords.append((r,c))
    return coords

def set_lbls_color(h:list, v:list, s, lg:list):
    coords = get_coordinates(h,v)
    color = s.get()
    for t in coords:
        (r,c) = t
        lg[r][c]['background'] = color

def clear_lbls_color(lg:list):
    for r in range(4):
        for c in range(4):
            lg[r][c]['background'] = ''

btt_set = ttk.Button(mainframe, width=3, text='Set', command=lambda: set_lbls_color(h_ckbx_str_array, v_ckbx_str_array, cbbx_color, lblgrid))
btt_set.grid(column=0, row=5)

btt_clr = ttk.Button(mainframe, width=3, text='Clr', command=lambda: clear_lbls_color(lblgrid))
btt_clr.grid(column=0, row=0)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()