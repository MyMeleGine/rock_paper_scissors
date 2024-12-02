import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
CHOICES = [ROCK, PAPER, SCISSORS]

USER_WIN_MESSAGE = "User has won!"
COMPUTER_WIN_MESSAGE = "Computer has won!"
TIE_MESSAGE = "It's a tie!"

user_score = 0
computer_score = 0
rounds_played = 0

print("Let's play rock paper scissors! I, the computer, am your opponent...")

def get_user_choice():
    while True:
        try:
            choice = input(f"Enter your choice ({ROCK}, {PAPER}, or {SCISSORS}): ").strip().lower()
            if choice not in CHOICES:
                raise ValueError
            return choice
        except ValueError:
            print(f"Invalid choice. Please enter '{ROCK}', '{PAPER}', or '{SCISSORS}'.")

def get_computer_choice():
    choice = random.choice(CHOICES)
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return TIE_MESSAGE
    if user_choice == ROCK and computer_choice == SCISSORS \
    or user_choice == PAPER and computer_choice == ROCK \
    or user_choice == SCISSORS and computer_choice == PAPER:
        return USER_WIN_MESSAGE
    
    return COMPUTER_WIN_MESSAGE

def play_game():
    global user_score, computer_score
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    round_result = determine_winner(user_choice, computer_choice)
    
    print(f"User chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    print(f"Result: {round_result}")

    if round_result == USER_WIN_MESSAGE:
        user_score += 1
    elif round_result == COMPUTER_WIN_MESSAGE:
        computer_score += 1

    print()
    print("▀▄▀▄▀▄ Scoreboard ▄▀▄▀▄▀")
    print(f"User Score: {user_score}")
    print(f"Computer Score: {computer_score}")
    print()
    
def yes_no(prompt):
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ["y", "n"]:
            return response == "y"

while True:
    play_game()
    rounds_played += 1

    again = yes_no("Do you want to play again?")
    if not again:
        print("gg")
        break
    
    print()
