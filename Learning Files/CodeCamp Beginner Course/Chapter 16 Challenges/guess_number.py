import sys
import random

# py guess_number.py -n "Dylan"
def guess_num(name='PlayerOne'):
    game_count = 0
    wins = 0

    def play_guess_num():
        nonlocal name
        nonlocal game_count
        nonlocal wins

        number = random.choice("123")

        player_guess = input(f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n")
        if player_guess not in ["1","2","3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            play_guess_num()
        game_count += 1

        if number == player_guess:
            wins += 1
            outcome = f"{name}, you win!"
        else:
            outcome = f"{name}, you lost.."

        print(f"\n{name}, you chose {player_guess}.\nI was thinking about the number {number}.\n\n{outcome}\n\nGame count: {game_count}\n\n{name}'s wins: {wins}\n\nYour winning percentage: {wins/game_count:.2%}\n\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_num()
        else:
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Cya {name}!")
            else:
                return

    return play_guess_num


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Inserts name when needed."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guessnum = guess_num(args.name)
    guessnum()