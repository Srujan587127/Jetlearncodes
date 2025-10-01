from tkinter import *

root = Tk()
root.geometry("450x250")
root.title("ROCK PAPER SCISSORS")

title = Label(root, text = "ROCK PAPER SCISSORS", font = 16)
title.grid(row = 0, column = 1, pady = 10)

btn_rock = Button(root, text = "ROCK", width = 12, font = 12, bg = "lightgrey")
btn_rock.grid(row = 1, column = 0, padx = 5, pady = 10)

btn_paper = Button(root, text = "PAPER", width = 12, font = 12, bg = "lightgrey")
btn_paper.grid(row = 1, column = 1, padx = 5, pady = 10)

btn_scissors = Button(root, text = "SCISSORS", width = 12, font = 12, bg = "lightgrey")
btn_scissors.grid(row = 1, column = 2, padx = 5, pady = 10)

root.mainloop()

