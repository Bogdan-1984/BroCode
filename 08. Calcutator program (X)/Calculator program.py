# Python calculator

'''operator = input("Enter an operator (+ - * /): ")
num1 = (input("Enter the first number: "))
num2 = (input("Enter the second number: "))

print(num1 + num2)'''

# Enter an operator (+ - * /): +
# Enter the first number: 10
# Enter the second number: 11
# RESULT: 1011
    # If executed as above, the result is a string concatenation of entered date. 10 and 11 in this case
# --------------------------------------------------------------------------------------------------------------

# The user input must be type-casted to float in this case, in order to add the numbers together.

'''operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(num1 + num2)'''

# Enter an operator (+ - * /): +
# Enter the first number: 10
# Enter the second number: 11
# RESULT: 21.0

# --------------------------------------------------------------------------------------------------------------

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
# If users input a non-existent operator stated above
else:
    print(f"{operator} is not valid operator")