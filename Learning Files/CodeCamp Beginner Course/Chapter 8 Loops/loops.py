# a while loop executes a block of code while a condition is true
value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break # the break keyword stops the loop completely
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue # the continue keyword skips the next steps and loops back around inless broken
#     print(value)
# else:  # else works like the falling action in action_over_time; it executes when the while is broken
#     print("value is now equal to " + str(value))

# a for loop iterates over a sequence

names = ['Dave', 'Sara', 'John'] # if it is a list, tuple or set it prints each value
# for x in names:
#     print(x)

# for x in "Mississippi": # if it is a string it prints each character
#     print(x)

# for x in names:
#     if x == 'Sara':
#         break
#     print(x)

# for x in names:
#     if x == 'Sara':
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(2,4): # includes the number that you start on and not the one you end on
#     print(x)

for x in range(5,105,5): # basically tell it to start from 0 end at 100 and increment by 5
    print(x)
else:
    print("Glad that's over")

names = ['Dave', 'Sara', 'John']
actions = ["codes", "eats", "sleeps"]

# for name in names: # nested loops
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")

# here is a simple way to make a prompt that only accepts some answers

while True:
    playagain = input("\nY for Yes or \nQ to Quit\n")
    if playagain.lower() not in ["y", "q"]:
        continue
    else:
        break

# how a for loop works because idk how

tasks = ["task1", "task2", "task3"]

for task in tasks:
    print("Doing", task)

# 1. Initialization: The for loop starts by looking at the first item in your list, tasks.
# 2. Iteration: It then takes each item one by one and assigns it to the variable task. It repeats this process for each item in the list.
# 3. Execution: Inside the loop, you can do something with each item. Here, we're just printing each task.
# 4. Termination: Once it has gone through all the items in the list, the loop ends.