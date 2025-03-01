# While loop = execute some code WHILE some condition remains TRUE

"""name = input("Enter your nane: ")

if name =="":
    print("You did not enter your name")
else:
    print(f"Hello {name}")"""
# -----------------------------------------------------------------------------------------------------------
# it will continuously prompt the user to enter a name, while display the print message.
"""name = input("Enter your nane: ")

while name =="":
    print("You did not enter your name")
    name = input("Enter your nane: ")
print(f"Hello {name}")"""

# -----------------------------------------------------------------------------------------------------------

# !!!!!
# This is an INFINITE LOOP. It will continuously ask to enter the name, without giving the option to enter it.

"""name = input("Enter your name: ")

while name =="":
    print("You did not enter your name")

print(f"Hello {name}")"""

# -----------------------------------------------------------------------------------------------------------

"""age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")"""

# -----------------------------------------------------------------------------------------------------------

"""food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("bye")"""

# -----------------------------------------------------------------------------------------------------------

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")