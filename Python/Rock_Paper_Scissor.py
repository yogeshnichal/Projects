# Create Rock Paper Scissor
# Play with Computer
# Get the input from user and print the result.
import random

user_choice = input("Enter your move(Rock, Paper, Scissor): ")
computer_choice = random.choice(["Rock", "Scissor", "Paper"])

if (user_choice == computer_choice):
    print("Match Tie")

elif user_choice == computer_choice:
    if user_choice == "Rock":
        if computer_choice == "Paper":
            print("Paper covers Rock, Computer win")
        else:
            print("Rock smashes Scissor, You won")
elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cuts paper, Computer wins")

    else:
        print("Paper cover Rock, Tou win")

elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("Rock smashes Scissor, Computer won")
    else:
        print("Scissor cuts paper, You won")
print(user_choice, computer_choice)