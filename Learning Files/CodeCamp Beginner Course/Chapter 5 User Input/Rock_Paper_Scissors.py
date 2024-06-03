import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2 
    SCISSORS = 3

# value = input('Please enter a value:\n') # waits for the user to make an input

# print("")
# print(value)

print("")
playerchoice = input("Enter...\n1 for Rock,\n2 for Paper, \n3 for Scissors:\n\n")

# if playerchoice != '1' or '2' or '3': # yo i figured it out myself :DDDD
#     sys.exit("\nPlease enter 1, 2, or 3.") # post-game edit - it did not work :((((

player = int(playerchoice) # converts input from string to integer

if player < 1 or player > 3:
    sys.exit("Please enter 1, 2, or 3.") # stops the game but also prints string on exit

computerchoice = random.choice("123") # will choose one of the characters from the string
computer = int(computerchoice) # converts input from string to integer

print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".") # using choice because it a string not an integer
print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

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

    playeraaaa = input("\nEnter any character to close!")