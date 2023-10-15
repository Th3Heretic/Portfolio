
# The long way to determine a data type
print("The data type of 'False' is", type(False))
print("The data type of '1000' is", type(1000))
print("The data type of '100.111' is", type(100.111))
print("The data type of 'Hello' is", type("Hello"))
print("The data type of 'True' is", type(True))
print("The data type of '100/5' is", type(100/5))
print("The data type of '100//5' is", type(100//5))

# Concatenation example of why a data type is so important because it can lead to logical runtime errors
print("10" + "10")
# The output is 1010 because it is adding the two strings together rather than performing an arithmetic operation

# Multiplying a string with an integer
print("ABC" * 10)
# It prints the string 10 times back to back
