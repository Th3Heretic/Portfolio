# The function calls automatically assume that the order of the passed formal parameters are the same as
# the passed actual parameter.

def somefunc(x, y, z):
    print("x =", x, "\ny =", y, "\nz =", z)

somefunc(1, 2, 3)

# However you can explicitly name your parameters
somefunc(y=99, z=11.5, x="dog")
# Which will return the values as defined by you
