
# Use case of a relational boolean operator
list = [1, 2, 3]
list1 = [1, 2, 2]

print("1, 2, 3 < 1, 2, 3 =", list < list)
print("1, 2, 2 < 1, 2, 3 =", list1 < list)

# Booleans between data types
# Integer to Float
print(5 < 10.2)
# Integer to string - Logical TypeError
# print(5 < "Monty")
# While this is an integer to an integer, the second one is held within a string and so results in a TypeError
# print(5 < "5")

# Booleans with Equality operators
print(5 == "5")
# These equality operators are slightly more forgiving when it comes to crossing numbers between strings
# This is False because the string value is not equal to the integer value
