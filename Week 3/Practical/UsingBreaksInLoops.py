# Using a break loop to stop a loop from executing when a condition has been reached
value = int(input("enter a number: "))
for n in range(2, value//2):
    if value % n == 0:
        print(value, "is not a prime number")
        break
    else:
        print(value, "is a prime number")
