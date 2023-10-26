# You can wrap a block of code in a defined function, so you can call the whole block of code
# instead of rewriting it separately
msg = "Executed correctly"

def displaytwice(msg):
    """Displays a message twice upon execution"""
    print(msg)
    print(msg)


displaytwice(msg)
# Demonstrates how to use and retrieve docstrings
print(help(displaytwice))
