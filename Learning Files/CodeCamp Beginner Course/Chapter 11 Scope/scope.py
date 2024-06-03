# gobal scope; avaliable to everything in the file

name = 'Dave'
count = 1
# local scope; only avaliable where it was defined
# def greeting(name):
#     color = "blue"
#     print(color)
#     print(name)

# greeting("john")
# print(color) # can't print because it was defined in the function and it was in a local scope

def another(): # another() is the parent scope which allows any nested scopes to access it
    color = 'Blue'
    # count = 2
    # count += 1
    # the variable can be accessed normally if  you wanted to print it but modification is not allowed
    global count
    count += 1 # must say that the variable is global in a different line before modification
    print(count) # if a variable with the same name as a global variable, the most local variable will be used
    def greeting(name):
        nonlocal color # accesses the parent scope
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()