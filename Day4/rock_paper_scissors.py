import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

if user_choice == computer_choice:
    print(f"Computer chose: {computer_choice}")
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissors" and computer_choice == "paper")):
    print(f"Computer chose: {computer_choice}")
    print("You win!")
elif user_choice in choices:
    print(f"Computer chose: {computer_choice}")
    print("You lose!")
else:
    print("Invalid input!")



