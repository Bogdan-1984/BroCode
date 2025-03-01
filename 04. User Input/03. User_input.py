# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

age = int(input("How old are you?: "))

age = age + 1

print("Happy Birthday")
print(f"You are {age} years old")
print(type(age))

# We can't normally user arithmetic expressions, we would have to type cast to an integer or a float.
