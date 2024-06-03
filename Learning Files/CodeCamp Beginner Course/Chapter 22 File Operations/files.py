import os
# os.chdir("C:/Users/sampl/OneDrive/Desktop/Coding Things/Learning Files/CodeCamp Beginner Course/Chapter 22 File Operations")

# RAWX acronym

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if doens't exist

f = open("names.txt") # if the action isn't specified it defaults to read

# print(f.read())
# print(f.read(4)) # once the file is read you can't re-read it returns "Dave"

# print(f.readline()) # reads the whole first line of the file
# print(f.readline()) # if it is run again it reads the second line since the first line has already been read

for line in f:
    print(line) # this will print eachline as if it were the example above

f.close() # it is important to close files so that you can see the change in the file if you did change something

try:
    f = open("name_list.txt") # this file doesn't exist
    print(f.read())
except:
    print("The file you wanted to read doesn't exist.")
finally:
    f.close()

# Append - creates a file if it doesn't exist

f = open("names.txt", "a")
f.write("Neil")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write - overwrites whatever is in the file

f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file is it does not exist

f = open("name_list.txt", "w")
f.close()

# Creates the specificed file, but returns an error if the file exists.

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete a file
# avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you want to delete does not exist.")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)