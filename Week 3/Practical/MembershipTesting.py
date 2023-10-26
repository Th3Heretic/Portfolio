
# You can use the membership tester 'in' to determine if a value appears in a list
names = ["Joe", "Jerry", "John", "Jeff", "Jose", "Jeremy"]

print("Joe" in names)

# The 'Not in' operator can be used in the same way
# This is great for username lists, so the same doesn't appear twice
print("Julie" not in names)

# You can also use this to search for keywords (snippets) within a string sentence
greeting = "Hello, I'm glad to see you again"

print("good" in greeting)
print("brilliant" not in greeting)
print("again" not in greeting)

# Expressions are used extensively throughout most programs, thus a thorough understanding
# of how to write these is of fundamental importance.
# Expressions are a very common source of logical errors, so always use operator precedence.
# Be aware that dynamically-typed languages such as Python allow a variable’s data-type to
# change at run-time
