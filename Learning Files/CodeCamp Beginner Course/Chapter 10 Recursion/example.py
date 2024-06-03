# this is basically review for while looks
value = True
while value == 1:
    print(value)
    value = 0 # remember 0 == False and 1 == True

value = "y"
while value: # just putting the variable asks "while variable exists"
    print(value)
    value = 0 

count = 0

while value:
    count += 1
    print(count)
    if count == 5:
        break
    else:
        value = 0
        continue # continue ends the current interation and skips to the next 

    