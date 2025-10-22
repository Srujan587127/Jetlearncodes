from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("Distance Calculator")

def calculate_distance():
    speed = entry_speed.get()
    time = entry_time.get()
    
    if speed == "" or time == "":
        text_result.delete("1.0", END)
        text_result.insert(END, "Please enter both speed and time!")
        return
    
    if not speed.isdigit() or not time.isdigit():
        text_result.delete("1.0", END)
        text_result.insert(END, "Please enter valid numbers!")
        return
    
    distance = int(speed) * int(time)
    text_result.delete("1.0", END)
    text_result.insert(END, str(distance) + " km")

title = Label(root, text="Distance Calculator", font=20)
title.grid(row=0, column=1)

label_speed = Label(root, text="Enter Speed (km/h):")
label_speed.grid(row=1, column=0)
entry_speed = Entry(root, width=10)
entry_speed.grid(row=1, column=1)

label_time = Label(root, text="Enter Time (h):")
label_time.grid(row=2, column=0)
entry_time = Entry(root, width=10)
entry_time.grid(row=2, column=1)

btn_calculate = Button(root, text="Calculate", bg="lightblue", command=calculate_distance)
btn_calculate.grid(row=3, column=1)

text_result = Text(root, width=20, height=2)
text_result.grid(row=4, column=1)

root.mainloop()