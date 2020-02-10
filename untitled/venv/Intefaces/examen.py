from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Buscaminas")

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
        x, y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x, y)
        try:
            target['background'] = event.widget['background']
            event.widget['background'] = ''
        except:
              pass

mainframe = ttk.Frame(root,relief='raised')




dnd = DragManager()
lblgrid = list()
for r in range(10):
    lblgrid.append([])
    for c in range(10):
        lblgrid[r].append(ttk.Label(mainframe, relief='groove'))
        lblgrid[r][c].grid(row=r+1, column=c+1, sticky='nwse')
        dnd.add_dragable(lblgrid[r][c])


for r in range(4):
    lblgrid.append([])
    for c in range(4):
        lblgrid[r].append(ttk.Label(mainframe, relief='groove'))
        lblgrid[r][c].grid(row=r+1, column=c+1, sticky='nwse')
        dnd.add_dragable(lblgrid[r][c])


root.mainloop()