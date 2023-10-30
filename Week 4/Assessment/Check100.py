# Defining a function that tests whether an input is between 0 and 100 (Inclusive)
# This can be useful for age verifications on websites and apps
print("Do you know numbers up to 100")


def check100():
    """This is a simple function to determine whether a number is lower than 100 and returns a snarky comment"""
    num = input("Enter a number under 100: ")
    if num == int:
        num = int(num)
        if num <= 100:
            print("Well done, you can follow instructions :)")
        else:
            print("Come on, you know that's not under 100")
    else:
        if num == "":
            print("You didn't think to enter something, no?")
        elif num:
            print("That's not a number and you know it")


# Testing this function in a program
check100()
