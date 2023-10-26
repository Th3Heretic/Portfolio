
# Using a while loop to act as a countdown
count = 10

while count > 0:
    print(count)
    count -= 1

# Using a for loop to print names in a list and add your own name to the list
name = ["Jerry", "John", "Jonah", "Jeff"]

name.append(input("What is your name? "))

print("Attendance for today is:")
for i in name:
    print(i)
