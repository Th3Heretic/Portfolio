# You can wrap a block of code in a defined function, so you can call the whole block of code
# instead of rewriting it separately
msg = "Executed correctly"


def displaytwice(msg):
    print(msg)
    print(msg)


displaytwice(msg)
