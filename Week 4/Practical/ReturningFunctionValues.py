# Finding the max of 2 values and then returning which one is higher
def findMax():
    """Finds the maximum of two values."""
    a = input("a: ")
    b = input("b: ")
    if ( a > b ):
        max = a
    else:
        max = b
    return max


print(findMax())
