import YtGUI.BasicApplication as basicApp
import YtGUI.DND.TkDND as tkDnd
import tkinter as tk


class DragFileApp(basicApp.BasicApplication):
    def create_widgets(self):
        dnd = tkDnd.TkDND(self.root)
        self.entry = tk.Entry()
        self.entry.pack()
        dnd.bindtarget(self.entry, self.drag_handle, 'text/uri-list')

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
        self.quit.pack()
        pass

    def drag_handle(self, event):
        event.widget.insert(0, event.data)

        pass


if __name__ == '__main__':
    DragFileApp().mainloop()

    pass
