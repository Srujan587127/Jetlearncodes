# def muilt_table(number):
#     for i in range(1,11):
#         result = number * i
#         print(f"{number} x {i} = {result}")

# muilt_table(4)

from tkinter import *

root = Tk()
root.geometry('400x300')
root.title("Multiplication Table")

def create_table():
    num = entry_num.get()

    text_result.delete("1.0", END)

    num = int(num)

    for i in range(1,11):
        result = num * i
        text_result.insert(END, f"{num} x {i} = {result},")
    


Label(root, text = "MULTIPLICATION TABLE", font = 20).grid(row=0, column = 1, pady = 5)


Label(root, text = "enter a number:", font = 20).grid(row=1, column = 0)
entry_num = Entry(root, width=10)
entry_num.grid(row=1, column= 1)

Button(root, text = "Table", bg = "light blue", command = create_table).grid(row=2, column=1, pady=5)

text_result = Text(root, width=25, height = 12)
text_result.grid(row =3, column=1)

root.mainloop()
