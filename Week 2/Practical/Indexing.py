
# Indexing allows you to call a specific character within a string by using square brackets
surname = "Snow"
initial = surname[0]
print(initial)

# An error occurs when you call a character out of the string's range
#surname = "Palin"
#initial = surname[10]
#print(initial)

#   initial = surname[10]
#IndexError: string index out of range

# You can also use negative indexes to call characters starting from the back of the string starting from -1
surname = "Snow"
initial = surname[-1]
print(initial)
