#
def my_func():
    one = input("Num 1: ")
    two = input("Num 2: ")

    if two == "":
        one = int(one)
        result = one * one
    elif one == "":
        two = int(two)
        result = two * two
    else:
        two = int(two)
        one = int(one)
        result = one * two

    print(result)


my_func()
