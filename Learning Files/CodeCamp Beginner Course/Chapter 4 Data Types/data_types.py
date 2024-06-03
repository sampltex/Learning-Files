# String data type

# literal assignment
first = 'John'
last = 'Doe'

# print(type(first))
# # print(type(first) == str) gives boolean output if it is T or F
# print(type(first) == str)
# # is the first variable an instance (object) of srt, returns T
# print(isinstance(first, str))

# #constructor function
# pizza = str('Pepperoni') # same as pizza = 'pepperoni' just gives instance of a string
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# ^ these are both ways assign string data to variables ^

# a literal assignment is first = 'John'
# a constructor function is first = str(john)

# concatenation
fullname = first + ' ' + last
print(fullname)
# basically just addition, literally

# fullname += '!' is the same as fullname = fullname + '!'
fullname += '!'
print(fullname)

# casting a number to a string
decade = str(2012)
print(type(decade))
print(decade)
# important because it is NOT a number it is a string
# bascially decade = 2012 vs. decade = '2012' but easier to see
# decade = str(2012) is the same as decade = '2012'

statement = 'I like video game music from ' + decade + 's.'
print(statement)

#  multiple lines
multiline = '''
Hey, how are you?                                           

I was just checking in.                                  

                                All good?

'''
print(multiline)

# ''' opening and ''' closing enables multiline string assignments
# like how javascript comments can be multilined with /* and */

# escaping special characters

# \ by itself allows for words like "I'm" to be made without problem
# \t is a tab in the string and \n is a new line in the string
# \ itself can be escaped by adding another on and it will print normally
sentence = 'I\'m still a piece of garbage.\t Yo!\n\nWhere\'s this at\\located?'
print(sentence)

# string methods
# (methods called upon the string class) (wtf is that this is chapter 4)

# the method itself is accessed by putting the little period after the var, there are MANY methods
print(first)
print(first.lower())
print(first.upper())
print(first)
# printing it again to show that the var first does not change only modified to print

print(multiline.title())
print(multiline.replace('good', 'ok'))
print(multiline)
# .title is propercase (capitalizes every first letter of every word)
# .replace replacese every instance of the string 'good' with the string 'ok'

# len() is the a function that find and prints the length of the var in the ()
# using the len() function does NOT print the var multiline
print(len(multiline))
multiline += '                  '
multiline = '                 ' + multiline
print(len(multiline))
# the first multiline modification adds characters to the end, and the second modification adds characters to the beginning

# .strip method removes white space characters (.rstrip is right strip and .lstrip is left strip)
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print('')

# build a menu
title = 'menu'.upper()
# the .upper method is stored in the title var
print(title.center(20, '='))
# centers the title between 20 of the string '=', resulting in 10 '=' on each side
print('Coffee'.ljust(16, '.') + '$1'.rjust(4))
print('Muffin'.ljust(16, '.') + '$2'.rjust(4))
print('Eggs'.ljust(16, '.') + '$4'.rjust(4))
# .ljust is left justify and .rjust is right justify 
# (google): returns a left-justified string according to the width specified and fills the remaining spaces with blank spaces if the character argument is not passed.
# .ljust() is anchored to the left side of the terminal and the number is the number of characters that the string prints to
# for example .ljust(16, '.') will print 16 periods of length from the left side of the terminal
# .rjust() is the same thing but anchored to the end of the left just

print('')

# string index values
print(first[1])
# the [] is basically a array from 0 to ...inf of each character in the string
# so since the first value [1] of the first var (John) is J then it prints J
print(first[-1])
# it starts from 0 so -1 loops back around (basically the last value in the string)
print(first[1:-1])
# the value you give at the end of the range will not be part of the output
print(first[1:])
# not providing a final value goes to all the way to the end of the var

print('')

# some methods return boolean data
print(first.startswith('J'))
print(first.endswith('a'))

# boolean data type
myvalue = True
# bool() is the constructor function like str()
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# numberic data type

print('')

#integer type
price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, bool))

print('')

# float data type
gpa = 4.00
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

print('')

# complex data type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print('')

# built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

# rounds to the nearest integer
print(round(gpa))
# rounds to the nearest first decimal point
print(round(gpa, 1))

print('')

import math # you'd usually type imports at the top of the file

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

print('')

# casting a string to a number

# the advantage of using a constructor function is that you can change the data type
# like here the zipcode is changed from a string to a integer

zipcode = '30269'
zip_value = int(zipcode)
print(type(zip_value))

# error if you attempt to cast incorrect data
# zip_value = int('new york')