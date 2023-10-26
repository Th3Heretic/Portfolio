# You can wrap a block of code in a defined function, so you can call the whole block of code
# instead of rewriting it separately

def displaytwice(msg):
    """Displays a message twice upon execution"""
    print(msg)
    print(msg)


displaytwice(msg)
# Demonstrates how to use and retrieve docstrings
print(help(displaytwice))

# When defining functions, there are Actual and Formal parameters:
#   Formal parameters are defined within the function and can only be called from within that function then
#   cease to exist once the block has executed.
#   Actual parameters are bound to the formal parameter.
