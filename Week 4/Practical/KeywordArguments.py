# The function calls automatically assume that the order of the passed formal parameters are the same as
# the passed actual parameter

def somefunc(x, y, z):
    print("x =", x, "\ny =", y, "\nz =", z)

somefunc(1, 2, 3)

# However you can explicitly name your parameters
somefunc(y=99, z=11.5, x="dog")
# Which will return the values as defined by you
# The only caveat being that it requires all parameters to be defined

# You can write it in a way where not all parameters must be defined for the code to run valid
def showMsg(title, body = "", prefix = "INFO:", suffix = "."):
    print(prefix, title, body, suffix)

# And you may call it without producing an error in a way such as:
showMsg("file opened")
showMsg("File not opened", prefix = "Error:")
showMsg("File missing", body="Insert Disk", suffix="Press return")
