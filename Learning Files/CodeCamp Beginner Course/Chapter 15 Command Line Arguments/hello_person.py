# MOVE FILE OUTSIDE OF CHAPTER FOLDER TO RUN
# YOU CANNOT RUN THE FILE WITH THE PLAY BUTTON USE "py hello_person.py" FOLLOWED BY APPROPRIATE IMPUTS TO RUN IT
def hello(name, lang, mood):
    greetings = { # create a dictionary if there are choices
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo"
    }
    moods = {
        "Happy": "!",
        "Unhappy": ""
    }
    msg = f"{greetings[lang]} {name}{moods[mood]}"
    print(msg)

if __name__ == '__main__':
    import argparse
    # parsing is breaking down files/data into smaller things that can be changed easily
    # for example converting a string to a list

    parser = argparse.ArgumentParser( # sets var parser to an argument parser (breaks down arguemnts?)
        description="Provides a personal gretting."
    )

    parser.add_argument( # adds argument to our arguement parser
        "-n", "--name", metavar="name", dest="firstname", # -n is a command like how quit() exits python
        required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English","Spanish","German"],
        help="The language of the greeting." # help is what is listed when the help command is inputted
    )

    parser.add_argument(
        "-m", "--mood", metavar="mood", # metavar is what the argument is refered to in the code
        required=True, choices=["Happy","Unhappy"],
        help="Sets the mood of the greeting."
    )

    args = parser.parse_args()

    hello(args.firstname, args.lang, args.mood)

    
