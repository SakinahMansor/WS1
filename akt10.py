#!/usr/bin/env python

import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors.")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    print(f"Computer's choice: {computer_choice}")
    print(f"Your choice: {user_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    rock_paper_scissors()