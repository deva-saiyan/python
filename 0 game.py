import random
import enum

# Define an Enum for choices
class Choice(enum.Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

try:
    player_choice = int(input("Enter a choice!\n 1 for Rock \n 2 for Paper \n 3 for Scissors \n"))

    if player_choice in [1, 2, 3]:  # Ensures input is valid
        computer_choice = random.choice([1, 2, 3])  # Picks a random choice as an integer

        # Print choices with their names from Enum
        print("Player Choice:", Choice(player_choice).name)
        print("Computer Choice:", Choice(computer_choice).name)

        # Determine the winner
        if player_choice == computer_choice:
            print("Game Tie....")
        elif (player_choice == 1 and computer_choice == 3) or \
             (player_choice == 2 and computer_choice == 1) or \
             (player_choice == 3 and computer_choice == 2):
            print("You Win!")
        else:
            print("Computer Wins!")

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

except ValueError:  # Catches invalid (non-integer) inputs
    print("Enter a number, not a string!")
