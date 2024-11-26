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
    if user_choice == "Paper" and computer_choice == "Rock":
        return "User Wins!"
    if user_choice == "Scissors" and computer_choice == "Paper":
        return "User has won!"
    
    return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    round_result = determine_winner(user_choice, computer_choice)
    
    print(f"User chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    print(f"Result: {round_result}")

while True:
    play_game()
    again = input("Do you want to play again? (y/n): ") in ["y", "yes"]
    if not again:
        print("GG")
        break
    
