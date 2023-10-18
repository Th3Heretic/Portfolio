
# Using 'and', 'or' & 'not' statements
age = int(input("How old are you? "))
print(age>=18 and age<=65)

print(age<18 or age>65)

print(not age>18)

# Using multiple expressions in a single statement
print((age>=18 and age<=65) and (not age==30))
