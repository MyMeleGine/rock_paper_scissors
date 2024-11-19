import random

print("Let's play Rock, Paper, Scissors")
def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ")
    return choice

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    choice = random.choice(choices)
    return choice

print(get_user_choice())
print(get_computer_choice())
