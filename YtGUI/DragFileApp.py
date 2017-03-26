import YtGUI.BasicApplication as basicApp
import YtGUI.DND.TkDND as tkDnd
import tkinter as tk
from tkinter import *


class DragFileApp(basicApp.BasicApplication):
    def create_widgets(self):
        self.label = tk.Label(self, text="drag the file in:")
        self.label.pack()

        self.frame = tk.Frame(self, width=400, height=300, bg="red", colormap="new")
        self.frame.pack()

        dnd = tkDnd.TkDND(self.root)
        self.entry = tk.Entry(self, width=60)
        self.entry.pack()
        dnd.bindtarget(self.frame, self.drag_handle, 'text/uri-list')

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
        self.quit.pack()
        pass

    def drag_handle(self, event):
        # event.widget.insert(0, event.data)

        data_str = event.data

        print(data_str)
        self.entry.delete(0, END)
        self.entry.insert(0, data_str[1:-1])
        pass


if __name__ == '__main__':
    DragFileApp().mainloop()

    pass
