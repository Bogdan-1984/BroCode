
'''name = input("Enter your name: ")

if name == "":
    print("You did not type in your name")
else:
    print(f"Helloo {name}")'''

# -------------------------------------------------------------------------------------------

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name")
if name != "":
    print(f"Helloo {name}")

# != is the "not equal to" operator.
# name != "" checks if name is not an empty string.
# If name contains any characters (meaning the user entered something), the condition evaluates to True.