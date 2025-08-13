from tkinter import *
window = Tk()
window.title("Hello world")
window.geometry("300x300")

hello = Label(text = "Hello world!", background = "yellow", foreground = "red")
hello.pack( side = "left")
button = Button(text = "Click me!")
button.pack( side = "right")

button1 = Button(text = "Click me 2")
button1.pack()


window.mainloop()
