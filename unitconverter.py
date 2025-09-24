from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("Unit Converter")

def from_kg():
    kg = float(entry_kg.get())

    gram = kg * 1000
    pound = kg * 2.20462
    ounce = kg * 35.274

    text_gram.delete("1.0", END)
    text_pound.delete("1.0", END)
    text_ounce.delete("1.0", END)

    text_gram.insert(END, gram)
    text_pound.insert(END, pound)
    text_ounce.insert(END, ounce)



title = Label(root, text = "Unit Converter", font = 20)
title.grid(row = 0, column=1)

label_kg = Label(root, text = "Enter the weight in Kg:")
label_kg.grid(row = 1, column = 0)

entry_kg = Entry(root, width = 10)
entry_kg.grid(row = 1, column = 1)

btn_convert = Button(root, text = "Convert", bg = "lightblue", command = from_kg)
btn_convert.grid(row = 1, column = 2)

label_gram = Label(root, text = "Gram", width = 12, bg = "lightgrey")
label_gram.grid(row = 2, column = 0)


label_pound = Label(root, text = "Pounds", width = 12, bg = "lightgrey")
label_pound.grid(row = 2, column = 1)

label_ounce = Label(root, text = "Ounces", width = 12, bg = "lightgrey")
label_ounce.grid(row = 2, column = 2)

text_gram = Text(root, width = "12", height = 2)
text_gram.grid(row = 3, column = 0)


text_pound = Text(root, width = "12", height = 2)
text_pound.grid(row = 3, column = 1)


text_ounce = Text(root, width = "12", height = 2)
text_ounce.grid(row = 3, column = 2)

root.mainloop()




