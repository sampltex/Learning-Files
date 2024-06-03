person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.") # basic concatenation

message = "\n%s has %s coins left." % (person, coins) # this is an example of f-strings
# it inserts "person" to the first %s and "coins" to the second one
print(message)

message = "\n{} has {} coins left.".format(person, coins) # this method of strings is called formatting
# it calls the method format and places the callers into the braces in the string
print(message)

message = "\n{1} has {0} coins left.".format(coins, person) # this is also formatting
# you can call the callers to a certain index in the string (in the braces) which will put them in the order following the rules of a list
print(message)

message = "\n{person} has {coins} coins left.".format(coins=coins, person=person) # this is also formatting
# instead of an index now you have a variable, now functions closer to a dictitonary
print(message)

player = {
    "person": "Dave",
    "coins": 3
}

message = "\n{person} has {coins} coins left.".format(**player) # this is also formatting
# pulls the value from the dictionary
print(message)

########################
# f-Strings

message = f"\n{person} has {coins} coins left." # this is an f-String
# the f simply inserts the value from the key into the alloted variable
print(message)

message = f"\n{person} has {2 * 5} coins left." # you can use integers
print(message)

message = f"\n{person.lower()} has {2 * 5} coins left." # you can use methods
print(message)

message = f"\n{player['person']} has {2 * 5} coins left." # you can use dictionaries
print(message)

########################
# you can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n") # the second braces has .2 to decide the amount of decimal and the f stands for "fixed"

for num in range(1,11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1,11):
    print(f"\n{num} divided by 4.52 is {num / 4.52:.2%}")