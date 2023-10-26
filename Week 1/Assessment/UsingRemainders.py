# Number of lab groups
number = [113, 175, 12]
for i in range (3):
    remainder = number[i] % 24
    divide = number[i] // 24
    print(number[i], "students will make", divide, "filled groups and", remainder, "students left over")