import math
import sys
import random as rdm# you can make an alias for a module by putting as after it
from enum import Enum
import georgia # you can make your own module in a different python file
# if the if statement wasn't there in the georgia module then the command would run right here
from rps7 import rock_paper_scissors

print(math.pi)

# sys.exit()
# random.choice("123")
rdm.choice("123")

# to list each function of a module out do this
for item in dir(rdm):
    print(item)

print("\n")

print(georgia.capital)
georgia.randomfunfact()

print(__name__) # returns __main__ which indicates the file that is being ran
print(georgia.__name__)

rock_paper_scissors()