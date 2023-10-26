# Putting students into groups
students = float(input("How many students do you have? "))
GroupSize = float(input("How large do you want the groups to be? "))
groups = students // GroupSize
rem = students % GroupSize

print("There will be", groups, "groups, With", rem, "remaining in the smaller group")
