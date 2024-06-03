# and lambda function is a single expression that returns a value

# lambda num : num * num # squares a number

# this is the same as
# def lambda_square(num):
#     num = num * num
#     return num

squared = lambda num : num * num # you can set a variable to a lambda
# if i had the right thing it would be formatted to
# def squared(num): return num * num
print(squared(2))

addTwo = lambda num : num + 2
print(addTwo(12))

sum_total = lambda a, b : a + b
print(sum_total(10, 8))

##################################
# lambdas are usually used inside of other functions as functions that don't need to be reused
# ok but the whole point of a function is to reuse code why do this bruh

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

##################################
# higher order functions are functions that take functions as arguements or returns functions as a result
# the function made above is an example of this

numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num : num * num, numbers) # map is built into python and runs the second argument(data) through the first argument(function)
# we use this and not for loops because its faster, easier and cleaner
# basically from my understanding the harder python is to read for your average joe the better it is
print(list(squared_nums))

odd_nums = filter(lambda num : num % 2 != 0, numbers) # filter is also built in and only returns the numbers that got the true result
print(list(odd_nums))

from functools import reduce # can be complex but here it just adds everything together

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr : acc + curr, numbers, 10)
print(total)
# there two things do the same thing, add up everything, then add 10
print(sum(numbers))

names = ['Dave Gray', 'John Doe', 'Dylan Willmes', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0) # the optional base at the end if not optional since we are using lists
print(char_count)
#################################

