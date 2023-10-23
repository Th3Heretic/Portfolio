# defining the name variable as an input
name = input("Hi, what is your name? ")

# If a name isn't entered, it will let you know
if name:
    print("Hi,", name + ", It's nice to meet you.")
else:
    print("Hello, Stranger.")

# Prompt to enter a password
password1 = input("Enter a password: ")
password2 = input("Enter your password again: ")

# Check if the same password is entered correctly the second time
if password1 == password2:
    print("Password set")
else:
    print("Passwords do not match")
