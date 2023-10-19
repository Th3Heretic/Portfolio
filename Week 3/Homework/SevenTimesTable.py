
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for num in range(13):
    print(num, "X 7 =", num * 7)

choice = int(input("Pick a number to multiply by 7: "))

for num in range(choice):
    print(num, "X 7 =", choice * 7)
