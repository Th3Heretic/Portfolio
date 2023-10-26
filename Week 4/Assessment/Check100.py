# Defining a function that tests whether an input is between 0 and 100 (Inclusive)
# This can be useful for age verifications on websites and apps
print("Do you know numbers up to 100")


def check100():
    """This is a simple function to determine whether a number is lower than 100 and returns a snarky comment"""
    num = int(input("Enter a number under 100: "))

    if num <= 100:
        print("Well done, you can follow instructions :)")
    else:
        print("You know that number isn't under 100")


# Testing this function in a program
check100()
