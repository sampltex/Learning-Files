import sys
import random
from enum import Enum


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2 
        SCISSORS = 3


    # value = input('Please enter a value:\n') # waits for the user to make an input

    # print("")
    # print(value)

    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper, \n3 for Scissors:\n\n")

    # if playerchoice != '1' or '2' or '3': # yo i figured it out myself :DDDD
    # sys.exit("\nPlease enter 1, 2, or 3.") # post-game edit - it did not work :((((
    
    if playerchoice not in ["1","2","3"]: #  in returns True if value is found in the sequence
        print("Please enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice) # converts input from string to integer

    computerchoice = random.choice("123") # will choose one of the characters from the string
    computer = int(computerchoice) # converts input from string to integer

    print("You chose " + str(RPS(player)).replace("\nRPS.", "") + ".") # using choice because it a string not an integer
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")
    

    if player == 1 and computer == 3:
        print("🎉 You win! 🎉")
    elif player == 2 and computer == 1:
        print("🎉 You win! 🎉")
    elif player == 3 and computer == 2:
        print("🎉 You win! 🎉")
    elif player ==  computer:
        print("🤯 Tied game! 🤯")
    else:
        print("🐍 Python Wins! 🐍")

    print("\nPlay again?")

    while True:
        
        playagain = input("\nY for Yes \nN for No\n")
        if playagain.lower() not in ["y", "n"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n👋 Thank you for playing! 👋")
        sys.exit("Bye!")

play_rps()