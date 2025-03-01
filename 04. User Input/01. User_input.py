# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

'''input("What is your name?: ")'''
# The input function is going to return some data as a string.
# The data is written by a user answering the question above.
# Nothing else happens after the user inputs his answer.

# We can assign it to a variable.
name = input("What is your name?: ")
print(f"Hello {name}")

age = input("How old are you?: ")
age = age + 1

print(age)

# RESULT
#    age = age + 1
# TypeError: can only concatenate str (not "int") to str

# 1 is a int, when we accept the user input we store that input as a string