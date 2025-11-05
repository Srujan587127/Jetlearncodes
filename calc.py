from tkinter import *

root = Tk()
root.geometry("400x250")
root.title("Simple Calculator")

def calculate_result():
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    op = entry_operator.get()
    
    text_result.delete("1.0", END)
    
    if num1 == "" or num2 == "" or op == "":
        text_result.insert(END, "Please fill all fields!")
        return
    
    num1 = float(num1)
    num2 = float(num2)
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        text_result.insert(END, "Invalid operator! Use +, -, *, /")
        return
    
    text_result.insert(END, "Result: " + str(result))

Label(root, text="Calculator", font=20).grid(row=0, column=1, pady=5)

Label(root, text="Enter 1st Number:").grid(row=1, column=0)
entry_num1 = Entry(root, width=10)
entry_num1.grid(row=1, column=1)

Label(root, text="Operator (+ - * /):").grid(row=2, column=0)
entry_operator = Entry(root, width=10)
entry_operator.grid(row=2, column=1)

Label(root, text="Enter 2nd Number:").grid(row=3, column=0)
entry_num2 = Entry(root, width=10)
entry_num2.grid(row=3, column=1)

Button(root, text="Calculate", bg="lightgreen", command=calculate_result).grid(row=4, column=1, pady=5)

text_result = Text(root, width=25, height=2)
text_result.grid(row=5, column=1)

root.mainloop()
