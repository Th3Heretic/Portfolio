# Use this to determine how many sweets you will need
sweets = int(input("How many sweets do you have? "))
pupils = int(input("How many pupils are present today? "))
each = float(sweets // pupils)
left = float(sweets % pupils)

print("You will have given", pupils,"pupils, a total of", each, "sweets each, and you have", left, "sweets leftover")