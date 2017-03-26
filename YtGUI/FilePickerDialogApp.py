import YtGUI.BasicApplication as basicApp
from tkinter import filedialog
import tkinter as tk


class FilePickerDialogApp(basicApp.BasicApplication):
    def create_widgets(self):
        self.browse_button = tk.Button(self, text="Browse", command=self.load_file)
        self.browse_button.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
        self.quit.pack()
        pass

    def load_file(self):
        file_path = filedialog.askopenfilename()
        print(file_path)


if __name__ == '__main__':
    FilePickerDialogApp().mainloop()

    pass
