
# Slicing allows you to call multiple characters within a string in a range
surname = "Snow"
initial = surname[0:2]
print(initial)
# Notice how the start value is included and the end value is excluded

# By omitting a start or end value, the program will default to the start or end of the string
name = "Damien Snow"
initial = name[:5]
print(initial)

name = "Damien Snow"
initial = name[4:]
print(initial)

# If you omit both values, it will just include the whole string
name = "Damien Snow"
initial = name[:]
print(initial)
# Note the output in the console at the bottom

# Using a value that is outside the range of the string, an error is not reported, but is rather just ignored
name = "Damien Snow"
initial = name[7:15]
print(initial)
