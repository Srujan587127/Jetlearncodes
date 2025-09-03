from tkinter import *

top = Tk()
top.title("My favorite Dishes")

listbox = Listbox(top , height = 10,
                  width = 15,
                  bg = "grey",
                  activestyle = "dotbox",
                  font = "Helvetica",
                  fg = "yellow")


top.geometry("300x250")

label = Label(top, text = "FOOD ITEMS")

listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")   
listbox.delete(3)

label.pack()
listbox.pack()

top.mainloop()