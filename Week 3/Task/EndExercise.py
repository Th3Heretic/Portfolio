# Defining the list
numbers = [10, 20, 30, 90, 200, 30, 22, 11]
limit = 100
total = 0
error = "Error: Number found over 100"
var = 0

for num in numbers:
    if num > limit:
        print(error)
        break
    else:
        total += num
        var += 1
        print(total)
        continue

if var == len(numbers):
    print("All numbers processed")
