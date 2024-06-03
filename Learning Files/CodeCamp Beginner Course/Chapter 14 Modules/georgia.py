from random import choice

capital = "Atlanta"

bird = "Brown Thrasher"

flower = "Cherokee Rose"

song = "Georgia On my Mind"

def randomfunfact():
    funfacts = [
        "Georgia is cool",
        "Georgia is awesome",
        "I live there"
    ]

    index = choice("012")

    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()