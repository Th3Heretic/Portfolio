
# These are similar to an 'if' statement but is written on a single line, instead of multiple
num1 = input("Enter number one: ")
num2 = input("Enter number two: ")

highest = num1 if num1 > num2 else num2
print(highest)

# Another way to write that is:
num3 = input("Enter number three: ")
num4 = input("Enter number four: ")

if num3 > num4:
    highest = num3
else:
    highest = num4

print("The highest is: ", highest)