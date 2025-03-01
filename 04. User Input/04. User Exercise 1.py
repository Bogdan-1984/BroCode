# Exercise 1 Rectangle Area calculator

"""length = input("Enter the length: ")
width = input("Enter the width: ")
area = length * width

print(area)"""
# TypeError: can't multiply sequence by non-int of type 'str'

# ---------------------------------------------------------------------------------------------------------

"""length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(area)"""

# Enter the length: 5
# Enter the width: 6
# RESULT: 30.0 (because it's a float variable)

# ---------------------------------------------------------------------------------------------------------

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is: {area}cm²")
# Enter the length: 6.1
# Enter the width: 7.2
# The area is: 43.92cm²