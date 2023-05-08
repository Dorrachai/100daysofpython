import random

choices = ["rock", "paper", "scissors"]
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = input("Enter your choice (rock/paper/scissors): ")

# Validate the user's choice
while user_choice not in choices:
    user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ")

computer_choice = random.choice(choices)

# The user's choice
print(f"You chose {user_choice}.")
if user_choice == "rock":
    print(rock)
elif user_choice == "paper":
    print(paper)
else:
    print(scissors)

# The computer's choice
print(f"The computer chose {computer_choice}.")
if computer_choice == "rock":
    print(rock)
elif computer_choice == "paper":
    print(paper)
else:
    print(scissors)

# Winner
if user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
else:
    print("You lose.")