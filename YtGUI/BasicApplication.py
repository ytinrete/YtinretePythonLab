import tkinter as tk
import YtGUI.DND.TkDND as tkDnd


# from tkinter import *

class BasicApplication(tk.Frame):
    def __init__(self, root=None):
        self.root = root
        super().__init__(root)
        self.pack()
        self.fix_window()
        self.create_widgets()

    def fix_window(self):
        w = 800  # width for the Tk root
        h = 600  # height for the Tk root

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.master.title("Application")
        # self.master.size(800, 600)
        # self.master.maxsize(1000, 400)

    def create_widgets(self):
        self.label = tk.Label(self, text='Label')
        self.label.pack()

        self.hi_there = tk.Button(self, text='button')
        self.hi_there["command"] = self.on_button_click
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
        self.quit.pack(side="bottom")

        dnd = tkDnd.TkDND(self.root)

        self.entry = tk.Entry()
        self.entry.pack()

        dnd.bindtarget(self.entry, self.drag_handle, 'text/uri-list')

    def drag_handle(self, event):
        event.widget.insert(0, event.data)

        pass

    def on_button_click(self):
        print("on_button_click call!")


if __name__ == '__main__':
    app = BasicApplication(root=tk.Tk())
    app.root.attributes("-topmost", True)
    app.mainloop()

    pass
