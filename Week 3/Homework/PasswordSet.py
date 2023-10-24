# Defining a list of bad passwords
bad_passwords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# defining the name variable as an input
name = input("Hi, what is your name? ")

# If a name isn't entered, it will let you know
if name:
    print("Hi,", name + ", It's nice to meet you.")
else:
    print("Hello, Stranger.")

# Prompt to enter a password
password = input("Enter a password (8-12 chars): ")
passwordcheck = input("Enter your password again: ")

# Check if the same password is entered correctly the second time, is the correct length and isn't in the bad password list
for pass_check in bad_passwords:
    if password[7:13]:
        if password == passwordcheck:
            if not password == pass_check:
                print("Password Set :)")
                break
            else:
                print("Password Too Common")
                break
        else:
            print("Passwords must match")
    else:
        print("Passwords must be between 8 and 12 characters long")
