
# The 'if' statement is used for specifying the criteria for a specific portion of the program to run
age = int(input("How old are you? "))

# The 'if' statement executes code if the expression equates to true
if age > 70:
    print("Wow, well done for making it this far.")
# And the 'elif' statement executes if the expression has hit multiple criteria
# 'elif' must be put after 'if' but before 'else'
# This is because it makes the logic cascade, if the 'if' is false, then it will check the 'elif's
# and if they're false then it will check the final 'else' in the program and execute that
# You can have multiple 'elif' statements in your code for different outcomes
elif age > 45:
    print("You are pretty old.")
# The 'else' statement executed if the expression is false
else:
    print("You're still a young buck, congrats.")

