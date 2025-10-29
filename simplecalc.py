from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("400x200")
root.title("addition Calulator")

def calculate_sum():
    num1 = entry_num1.get()
    num2 = entry_num2.get()
 
    result = int(num1) + int(num2)
    tkinter.messagebox.showinfo("Result", "The sum is :" + str(result) )


title = Label(root, text = "Addition Calculator", font = 20)
title.grid(row = 0, column = 1)

label_num1 = Label(root, text = "Enter first number:")
label_num1.place(x=10, y=50)
entry_num1 = tkinter.Entry(root, width = 15)
entry_num1.place(x=150, y=50)

label_num2 = Label(root, text = "Enter second number:")
label_num2.place(x=10, y=90)
entry_num2 = tkinter.Entry(root, width = 15)
entry_num2.place(x=150, y=90)

btn_calculate = tkinter.Button(root, text = "Add", command = calculate_sum)
btn_calculate.place(x=150, y=130, height=28)

root.mainloop()