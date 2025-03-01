import math

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

# print(f"The circumference is: {circumference}")
    # entered value is :10.5
    # result is: 65.97344572538566

print(f"The circumference is: {round(circumference, 2)} cm")
    # if the variable is written as {round(VARIABLE, 2)}, it will truncate the result to 2 digits.