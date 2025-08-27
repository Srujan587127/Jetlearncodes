from tkinter import *
from tkinter.ttk import *
from time import strftime


root = Tk()
root.title("Menu Demonstration")
root.geometry("250x250")
root.config(bg = "black")

menubar = Menu(root)

file = Menu(menubar, tearoff=1)
menubar.add_cascade(label = "file", menu = file)
file.add_command(label = "New File", command = None)
file.add_command(label = "Open...", command = None)
file.add_command(label = "Save", command = None)
file.add_separator()
file.add_command(label = "Exit", command = root.destroy)

edit = Menu(menubar, tearoff=1)
menubar.add_cascade(label = "edit", menu = edit)
edit.add_command(label = "undo", command = None )
edit.add_command(label = "redo", command = None)
edit.add_command(label = "cut", command = None )
edit.add_command(label = "copy", command = None)
edit.add_separator()
edit.add_command(label = "paste", command = None)





root.config(menu = menubar)     

mainloop()
    


