import random

def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ")
    return choice

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    choice = random.choice(choices)
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if user_choice == "Rock" and computer_choice == "Scissors":
        return "User wins!"
    if user_choice == "Rock" and computer_choice == "Paper":
        return "Computer Wins, you lost!!!"
    if user_choice == "Paper" and computer_choice == "Scissors":
        return "Computer wins!"
    if user_choice == "Paper" and computer_choice == "Rock":
        return "User Wins!"
    if user_choice == "Scissors" and computer_choice == "Paper":
        return "User has won!!"
    if user_choice == "Scissors" and computer_choice == "Rock":
        return "YOU lost against a computer!!!"
    
    return "how did we get here"


def play_game():
    print("Let's play Rock, Paper, Scissors")


user_choice = get_user_choice()
computer_choice = get_computer_choice()

print(f"User chose: {user_choice}")
print(f"Computer chose: {computer_choice}")
