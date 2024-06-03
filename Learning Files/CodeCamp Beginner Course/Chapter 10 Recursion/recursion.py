# recursion is when a function calls itself
def add_one(num):

    if(num >= 9):
        return num + 1
    
    total = num + 1
    print(total)

    return add_one(total) # return basically "returns" the the value back to the caller, in this case the caller is "total"

mynewtotal = add_one(0)
print(mynewtotal)

hi = 0

while hi <= 9:
    hi = hi + 1
    print(hi)

print(hi)