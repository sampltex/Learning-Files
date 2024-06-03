# dictionaries are used to store data values in key value pairs
band = {
    "vocals": "Plants",
    "guitar": "Page"
}

# a key is the first value and the value is the second value
band2 = dict(vocals="Plants", guitar="Page")
# band and band2 are the same thing just declared differntly

print(band)
print(band2)
print(type(band))
print(len(band)) # len() tells you how many pairs there are instead of characters

# how to access items
print(band["vocals"])
print(band.get("guitar"))

print(band.keys()) # list all keys

print(band.values()) # list all values

# list of key/value pairs  as tuples
print(band.items())

# verify a key exists boolean
print("guitar" in band)
print("cowbell" in band)

# change values in dictionary
band["vocals"] = "Coverdale" # sets the value for the key vocals is now Coverdale and not Plants
band.update({"bass": "JPJ"}) # .update adds a new key/value pair to the dictionary

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # returns tuple, .popitem pops the more recently added item
print(band)

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear() # methods must have () after it
print(band2)

del band2

# copy dictionaries
# band2 = band # creates a reference not a copy, both refer to the same dicitonary
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy() # to copy something you must use the copy method, declaring it equal does not work
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# you can also use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)

# nested dictionaries
# the value of a key value pair can be another dictionary

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2,
}
print(member1)
print(member2)
print("")
print(band)
print(band["member1"]["name"]) # prints two levels deep, like a filepath: C:Desktop\Users

# sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(len(nums))
print(type(nums))

# no duplicates are allowed
nums = {1,2,2,3} # returns {1, 2, 3} just ignores the dupe
print(nums)

# True is a dupe of 1, False is dupe of 0

nums = {1, True, 2, False, 3, 4, 0} # ignores the second dupe of a value as seen the True being ignored and the 0 being ignored
print(nums)

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# add a new element to a set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples and dictionaries too

# merge two sets into one
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates from the sets
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

# keep everything by the duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)