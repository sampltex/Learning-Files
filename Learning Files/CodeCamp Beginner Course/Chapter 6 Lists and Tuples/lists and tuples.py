users = ['Dave', 'John', 'Sarah'] # lists are defined by using brackets

data = ['Dave', 42, True] # lists can have any type of data in them

emptylist =  [] # this is also a valid list

print("Dave" in emptylist) # returns boolean checking to see if the string Dave is in the list

print(users[0]) # prints Dave, retreives data from the list users position 0 (first position)
print(users[-1]) # prints Sarah, gives last value in list

print(users.index('Sarah')) # returns 2 since Sarah is in the second position

print(users[0:2]) # goes FROM the first position UNTIL the third position aka stops at third pos
print(users[0:]) # not giving a value to stop the list just lists everything from the first value given to the end of the list
print(users[-3:-1]) # going too far negative loops back around, the same as first users print

print(users[::-1]) # easy way to reverse a list (just for the print, to declare that it is reverses use list.reverse())

print(len(data)) # returns the number of objects in list, not characters

# various ways to add to a list

users.append('Ryan') # use the method .append to add objects to a list
print(users)

users += ['Jason'] # must be a list to add a list together otherwise adds each letter from string
print(users)

users.extend(['Robert', 'Ivan'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob') # first value of method is the position, the second is what we add
print(users)

# .append adds a single object and add it as it is.
# .extend adds a list and appends its objects individually to the list
# .extend adds to the end, .insert adds to the start

users[2:2] = ['Eddie', 'Alex'] # pick anywhere to insert by using bracket notation and picking the same value to start and end
print(users)

users[1:3] = ['Robert', 'Jimmy'] # this form of inserting replaces the previous list values
print(users)

# various ways to remove from a list

users.remove('Bob') # .remove takes from the start
print(users)

print(users.pop()) # .pop also returns the object but removess from the end of the list
print(users)

del users[0] # del can be used to delete any object
print(users)

#del data
data.clear()
print(data)

# various ways to sort a list

users[1:2] = ['dave']
users.sort() # .sort puts it into alphabetical ordor
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,5]
nums.reverse() # modifies the to be list reveresed
print(nums)

# nums.sort(reverse=True) # sorts it reversed, so sorts it from least to and then reverses it
# print(nums)

# ways to sort/modify a list non-destructively

print(sorted(nums, reverse=True)) # same as nums.sort(reverse=True) but only for the print
print(nums)

# all ways to copy a list
numscopy = nums.copy
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(numscopy)
print(mycopy)
print(mynums)

print(type(nums)) # can check the type of a list

mylist = list([1,'Neil', True]) # can make a list with a constructor function
print(mylist)

thing = ["h", "i", " ", "g", "u", "y", "s"]

thing = ' '.join(thing).replace(" ", "") # converts a list to a string
print(thing)

# tuples
# just like lists, but the data wil not change, and the order wil not change

mytuple = tuple(('dave',42,True))
anothertuple = (1,4,2,8,2,2) # defined by making a list using parenthesis instead of brackets

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple # this is called unpacking a tuple, the * takes the remaining values that havent been claim and takes it into a list
print(one)
print(two)
print(hey)

print(anothertuple.count(2)) # count counts the number of your argument that is in the tuple
# you can check how many methods there are for a data type by doing print(variable.) after the . all the methods will pop up
# tuples are more efficent than lists so use a tuple if you are not going to be changing a list