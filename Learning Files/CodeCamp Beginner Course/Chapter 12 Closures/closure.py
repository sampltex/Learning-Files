# Closure is a function having access to the scope of its parent function
# after the parent function has returned

def parnet_function(person, coins):
    # coins = 3
    # even if coins is defined above you can still access it since it is still in the parent function as a parameter
    def play_game():
        nonlocal coins # you don't need to make person nonlocal because you are not changing it
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game

# tommy = parnet_function("Tommy")
# jenny = parnet_function("Jenny")

# tommy()
# tommy()

# jenny()

# tommy()

tommy = parnet_function("Tommy", 3)
jenny = parnet_function("Jenny", 5)

tommy()
tommy()

jenny()

tommy()