from tkinter import *
import random

root = Tk()
root.geometry("450x300")
root.title("ROCK PAPER SCISSORS")

title = Label(root, text="ROCK PAPER SCISSORS", font=16)
title.grid(row=0, column=1, pady=10)

player_score = 0
computer_score = 0
choices = [("Rock", 0), ("Paper", 1), ("Scissors", 2)]

def get_computer_choice():
    return random.choice(choices)

def computer_wins():
    global computer_score, player_score
    computer_score += 1
    winner_label.config(text="Computer Won!!!")
    computer_score_label.config(text="Computer Score: " + str(computer_score))
    player_score_label.config(text="Player Score: " + str(player_score))

def player_wins():
    global computer_score, player_score
    player_score += 1
    winner_label.config(text="You Won!!!")
    computer_score_label.config(text="Computer Score: " + str(computer_score))
    player_score_label.config(text="Player Score: " + str(player_score))

def tie_game():
    winner_label.config(text="It's a Tie!")
    computer_score_label.config(text="Computer Score: " + str(computer_score))
    player_score_label.config(text="Player Score: " + str(player_score))

def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()
    player_choice_label.config(text="You Selected: " + player_input[0])
    computer_choice_label.config(text="Computer Selected: " + computer_input[0])

    if player_input == computer_input:
        tie_game()

    elif player_input[1] == 0: 
        if computer_input[1] == 1:  
            computer_wins()
        elif computer_input[1] == 2:  
            player_wins()

    elif player_input[1] == 1:  
        if computer_input[1] == 2:  
            computer_wins()
        elif computer_input[1] == 0: 
            player_wins()

    elif player_input[1] == 2:  
        if computer_input[1] == 0: 
            computer_wins()
        elif computer_input[1] == 1:  
            player_wins()



btn_rock = Button(root, text="ROCK", width=12, font=12, bg="lightgrey", command=lambda: player_choice(choices[0]))
btn_rock.grid(row=1, column=0, padx=5, pady=10)

btn_paper = Button(root, text="PAPER", width=12, font=12, bg="lightgrey", command=lambda: player_choice(choices[1]))
btn_paper.grid(row=1, column=1, padx=5, pady=10)

btn_scissors = Button(root, text="SCISSORS", width=12, font=12, bg="lightgrey", command=lambda: player_choice(choices[2]))
btn_scissors.grid(row=1, column=2, padx=5, pady=10)

player_choice_label = Label(root, text="You Selected: ", font=12)
player_choice_label.grid(row=2, column=0)

computer_choice_label = Label(root, text="Computer Selected: ", font=12)
computer_choice_label.grid(row=2, column=2)

winner_label = Label(root, text="", font=12, fg="blue")
winner_label.grid(row=3, column=1, pady=10)

player_score_label = Label(root, text="Player Score: 0", font=12)
player_score_label.grid(row=4, column=0)

computer_score_label = Label(root, text="Computer Score: 0", font=12)
computer_score_label.grid(row=4, column=2)

root.mainloop()
