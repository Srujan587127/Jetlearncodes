from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("Temperature Converter")

def from_celsius():
    c =  float(entry_c.get())

    f= (c * 9/5) + 32
    k = c + 273.15

    text_f.delete("1.0", END)
    text_k.delete("1.0", END)

    text_f.insert(END, f)
    text_k.insert(END, k)


title = Label(root, text="Temperature Converter", font=20)
title.grid(row=0, column=1)

label_c = Label(root, text="Enter temperature in °C:")
label_c.grid(row=1, column=0)

entry_c = Entry(root, width=10)
entry_c.grid(row=1, column=1)

btn_convert = Button(root, text="Convert", bg="lightblue", command=from_celsius)
btn_convert.grid(row=1, column=2)

label_f = Label(root, text="Fahrenheit (°F)", width=15, bg="lightgrey")
label_f.grid(row=2, column=0)

label_k = Label(root, text="Kelvin (K)", width=15, bg="lightgrey")
label_k.grid(row=2, column=1)

text_f = Text(root, width=15, height=2)
text_f.grid(row=3, column=0)

text_k = Text(root, width=15, height=2)
text_k.grid(row=3, column=1)

root.mainloop()