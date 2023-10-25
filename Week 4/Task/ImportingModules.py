# Importing whole module libraries can be done with >import [lib name]
import math

# Using that module needs to be done by prefixing the module name before the command
print(math.sqrt(2401))
# The 'sqrt' command calls for the square root operation to be performed

# You can just import sections from a module library with >from [lib name] import [lib function]
from math import sqrt

# This means you don't need to prefix the module name
print(sqrt(2401))

# calling the log function from the math module
from math import log2

# Using log2 in a formula
print(log2(1024))

# You can import all functions from the module using a wildcard(*)
# which means you don't need to prefix the module name to the function
from math import *

print("sqrt(49): ", sqrt(49))
print("cos(radians(45))): ", cos(radians(45)))

# Constant values can also be imported as well as the functions
from math import pi
print("Pi =", pi)
