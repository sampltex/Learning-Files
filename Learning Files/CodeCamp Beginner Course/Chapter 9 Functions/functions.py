# functions are reusable blocks of code, when it is called it runs the code in the function
def hello(): # create function by using define
    print("Hello world!") # need to be all lowercase can have underscores

hello() #call function by just using the name of it

# sometimes need to receive data, data is called parameters

def sum(num1, num2): # the stuff in the parenthesis is the parameters
    print(num1 + num2)

x = 2
y = 3

sum(x,y) # the stuff in the parenthesis when called is called an arguement (the data
sum(1,2)
sum(100,30)

def turn(a=3, num2=3): # the parameters in the function dont have to be anything they are just variables
    if (type(a) is not int or type(num2) is not int): # making the parameters equal to something only sets it if something isn't passed through the function in its place
        return 0 # if both parameters are black neither is used and instead returns "None"
    return a + num2

total = turn()
print(total)

def multiple(*args): # if you don't know how many arguments you're going to get use a * in front of your variable
    print(args)
    print(type(args)) # it is a tuple for some reason

multiple("Dave", "John", "Sara")

def mult_named_items(**kwargs): # i dont really know whats going on by if you put two asterices (**) it stands for key word arguements; same as one * but for key words ig
    print(kwargs)
    print(type(kwargs)) # it is a dictionary for some reason

mult_named_items(first = "Dave", Last = "Gray")

##### example of both being used #####
print("\n\n")
def order_pizza(size, *toppings, **details):
    print(f"Ordered a {size} pizza with the following toppins:")
    for topping in toppings:
        print(f"- {topping}")
    print("\nDetails of the order are:")
    for key, value in details.items():
        print(f"- {key}: {value}")

order_pizza("large","chicken","buffalo sauce", delivery=True, tip=5)