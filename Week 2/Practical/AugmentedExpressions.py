
# Using shorthand methods to express variable values
health = 100

print("You have", health, "health remaining")

health -= 1

print("You have", health, "health remaining")

health *= 4

print("""You picked up a medkit.
health remaining:""", int(health))

health /= 2

print("""You broke your leg.
Health remaining:""", int(health))
