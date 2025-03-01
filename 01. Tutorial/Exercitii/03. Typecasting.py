# Python Typecasting Exercises

# 1. Convert the integer `10` to a floating-point number.
exercise = "Exercise 1"
number = 10
float_number = float(number)
print(exercise)
print(float_number)
print()

# 2. Convert the string `"123"` to an integer.
exercise = "Exercise 2"
string_number = "123"
int_number = int(string_number)
print(exercise)
print(int_number)
print()

# 3. Convert the floating-point number `3.14` to an integer.
float_number = 3.14
int_number = int(float_number)
print("Exercise 3")
# print(int_number)
print(f"{int_number} (type: {type(int_number).__name__})") # Output: 3 (type: int)
print()

# 4. Convert the list `[1, 2, 3]` to a string.
list = [1, 2, 3]
str_list = str(list)
print("Exercise 4")
print(f"{str_list} (type: {type(str_list).__name__})")
print()

# 5. Convert the integer `255` to a hexadecimal string.
number = 255
hex_string = hex(number)
print("Exercise 5")
print(f"{number} => {hex_string}")
print()

# 6. Convert the boolean value `True` to an integer.
boolean_value = True
int_value = int(boolean_value)
print("Exercise 6")
print(int_value)
print()

# 7. Convert the string `"False"` to a boolean value.
str_value = "False"
boolean_value = bool(str_value)
print("Exercise 7")
print(boolean_value)
print()

# 8. Convert the string `"4.56"` to a floating-point number.
string_number = "4.56"
floating_number = float(string_number)
print("Exercise 8")
print(f"{floating_number} (type: {type(floating_number).__name__})")
print()


# 9. Convert the tuple `(1, 2, 3)` to a list.
tuple_numbers: tuple[int, int, int] = (1, 2, 3)
list_numbers = list(tuple_numbers)
print("Exercise 9")
print(list_numbers)
print()

# 10. Convert the integer `65` to a character.
int_number = 65
char_value = chr(int_number)
print("Exercise 10")
print(char_value)
print()

# 11. Convert the character `'A'` to its corresponding ASCII value.
char_value = "A"
ascii_value = ord(char_value)
print("Exercise 11")
print(ascii_value)
print()

# 12. Convert the string `"Hello"` to a list of characters.
string_value = "Hello"
list_characters = list(string_value)
print("Exercise 12")
print(list_characters)
print()

# 13. Convert the floating-point number `9.99` to a string.
float_number = 9.99
string_number = str(float_number)
print("Exercise 13")
print(f"{string_number} (type: {type(string_number).__name__})")
print()

# 14. Convert the string `"True"` to a boolean value using a method that returns `False` if the string is `"False"`.
str_value = "True"
boolean_value = str_value == "Ads"
print("Exercise 13")
print(boolean_value)
print()


# 15. Convert the list `[1, 2, 3]` to a tuple.
list_numbers = [1, 2, 3]
tuple_numbers = tuple(list_numbers)
print("Exercise 14")
print(f"{tuple_numbers} (type: {type(tuple_numbers).__name__})")
print()

# 16. Convert the floating-point number `2.718` to a string and then back to a floating-point number.
float_number = 2.718
str_value = str(float_number)
float_number_again = float(str_value)
print("Exercise 16")
print(f"{str_value} (type: {type(str_value).__name__})")
print(f"{float_number_again} (type: {type(float_number_again).__name__})")
print()

# 17. Convert the integer `42` to a binary string.
number = 42
binary_string = bin(number)
print("Exercise 17")
print(f"{number} = {binary_string} (type: {type(binary_string).__name__})")
print()

# 18. Convert the string `"1001"` to an integer using base 2 (binary).
binary_string = "1001"
int_value = int(binary_string, 2)
print("Exercise 18")
print(f"{int_value} (type: {type(int_value).__name__})")
print()

# 19. Convert the dictionary `{'a': 1, 'b': 2}` to a list of tuples.
dictionary = {'a': 1, 'b': 2}
list_of_tuples = list(dictionary.items())
print("Exercise 19")
print(list_of_tuples)
print()

# 20. Convert the string `"123.456"` to an integer, handling the error if the string cannot be directly converted.
string_number = "123.456"
try:
    int_number = int(string_number)
except ValueError:
    int_number = int(float(string_number))
print(int_number)