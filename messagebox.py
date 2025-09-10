from tkinter import *
from tkinter.ttk import *

from tkinter.filedialog import askopenfile

root = Tk()
root.geometry("200x100")

def open_file():
        file = askopenfile(mode = "r", filetypes = [("Text Files", '* .py')])
        if file is not None:
                content = file.read()
                print(content)

btn = Button(root, text = "Open", command = lambda:open_file())
btn.pack(side = TOP, pady = 10)

mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry("200x150")

def save():
    files = [("All Files", '*.*'),
             ("Python Files", "*.*"),
             ("Text Document", "*.txt")]
    file = asksaveasfile(filetypes = files, defualttextension = files)

btn = ttk.Button(root, text = "Save", command = lambda : save())

btn.pack(side = TOP, pady = 20)
messagebox.askyesno("Saving", "Are you sure you want to save?")
mainloop()

