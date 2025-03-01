# Exercise 1: Ask the user for their name and print a greeting message.
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Exercise 2: Ask the user for their age and print how old they will be in 10 years.
age = int(input("Enter your age: "))
future_age = age + 10
print(f"In 10 years, you will be {future_age} years old.")

# Exercise 3: Ask the user for two numbers and print their sum.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
print(f"The sum of the two numbers is: {sum_result}")

# Exercise 4: Ask the user for a number and print whether it is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Exercise 5: Ask the user for the radius of a circle and print the area.
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle is: {area}")

# Exercise 6: Ask the user for a temperature in Celsius and convert it to Fahrenheit.
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit}")

# Exercise 7: Ask the user for a word and print the word in reverse.
word = input("Enter a word: ")
reversed_word = word[::-1]
print(f"The word in reverse is: {reversed_word}")

# Exercise 8: Ask the user for a sentence and count the number of vowels in it.
sentence = input("Enter a sentence: ")
vowel_count = sum(1 for char in sentence if char.lower() in 'aeiou')
print(f"The number of vowels in the sentence is: {vowel_count}")

# Exercise 9: Ask the user for a number and check if it is a prime number.
number = int(input("Enter a number: "))
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")

# Exercise 10: Ask the user for a string and print the string in uppercase.
string = input("Enter a string: ")
uppercase_string = string.upper()
print(f"The string in uppercase is: {uppercase_string}")

# Exercise 11: Ask the user for a number and calculate the factorial of the number.
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is: {factorial}")

# Exercise 12: Ask the user for a number and check if it is a palindrome.
number = input("Enter a number: ")
if number == number[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

# Exercise 13: Ask the user for a number and print its multiplication table.
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Exercise 14: Ask the user for two numbers and print the greater one.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(f"The greater number is: {num1}")
elif num2 > num1:
    print(f"The greater number is: {num2}")
else:
    print("Both numbers are equal.")

# Exercise 15: Ask the user for a string and check if it contains the word "Python".
string = input("Enter a string: ")
if "Python" in string:
    print("The string contains the word 'Python'.")
else:
    print("The string does not contain the word 'Python'.")

# Exercise 16: Ask the user for a list of numbers (comma-separated) and print the sum.
numbers = input("Enter a list of numbers (comma-separated): ")
numbers_list = [float(num) for num in numbers.split(",")]
sum_result = sum(numbers_list)
print(f"The sum of the numbers is: {sum_result}")

# Exercise 17: Ask the user for a number and print its binary equivalent.
number = int(input("Enter a number: "))
binary = bin(number)[2:]
print(f"The binary equivalent of {number} is: {binary}")

# Exercise 18: Ask the user for a list of words (comma-separated) and print them in alphabetical order.
words = input("Enter a list of words (comma-separated): ")
words_list = sorted(words.split(","))
print(f"The words in alphabetical order are: {', '.join(words_list)}")

# Exercise 19: Ask the user for a number and print whether it is positive, negative, or zero.
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Exercise 20: Ask the user for a password and check if it is at least 8 characters long.
password = input("Enter a password: ")
if len(password) >= 8:
    print("The password is strong enough.")
else:
    print("The password is too short.")
