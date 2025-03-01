# 1. Write a program that asks the user for their name and then prints a greeting with their name.
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 2. Write a program that asks the user for two numbers and prints their sum.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"The sum is: {num1 + num2}")

# 3. Write a program that asks the user for their age and then tells them how old they will be in 10 years.
age = int(input("Enter your age: "))
print(f"In 10 years, you will be {age + 10} years old.")

# 4. Write a program that asks the user for the length and width of a rectangle and then calculates its area.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print(f"The area of the rectangle is: {length * width}")

# 5. Write a program that asks the user for a number and then checks if it is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# 6. Write a program that asks the user for a word and then prints it in reverse.
word = input("Enter a word: ")
print(f"The word in reverse is: {word[::-1]}")

# 7. Write a program that asks the user for a number and then prints its multiplication table up to 10.
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 8. Write a program that asks the user for a sentence and then counts the number of vowels in it.
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in sentence if char in vowels)
print(f"There are {count} vowels in the sentence.")

# 9. Write a program that asks the user for a string and then checks if it is a palindrome.
string = input("Enter a string: ")
if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

# 10. Write a program that asks the user for a number and then prints whether it is positive, negative, or zero.
number = float(input("Enter a number: "))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"The number is zero.")

# 11. Write a program that asks the user for a temperature in Celsius and then converts it to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F.")

# 12. Write a program that asks the user for a number and then finds its factorial.
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}.")

# 13. Write a program that asks the user for a list of numbers separated by spaces and then calculates their average.
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
average = sum(numbers) / len(numbers)
print(f"The average is: {average}")

# 14. Write a program that asks the user for their birth year and then calculates their age.
birth_year = int(input("Enter your birth year: "))
current_year = 2024
age = current_year - birth_year
print(f"You are {age} years old.")

# 15. Write a program that asks the user for a list of words separated by commas and then prints them sorted alphabetically.
words = input("Enter words separated by commas: ").split(",")
words.sort()
print("Sorted words: ", ", ".join(words))

# 16. Write a program that asks the user for a number and then prints the sum of all numbers from 1 to that number.
number = int(input("Enter a number: "))
total_sum = sum(range(1, number + 1))
print(f"The sum of all numbers from 1 to {number} is {total_sum}.")

# 17. Write a program that asks the user for two numbers and then checks if the first is divisible by the second.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num2 != 0 and num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}.")
else:
    print(f"{num1} is not divisible by {num2}.")

# 18. Write a program that asks the user for a string and then counts the number of words in it.
string = input("Enter a string: ")
words = string.split()
print(f"There are {len(words)} words in the string.")

# 19. Write a program that asks the user for a number and then finds the largest digit in it.
number = input("Enter a number: ")
largest_digit = max(number)
print(f"The largest digit in {number} is {largest_digit}.")

# 20. Write a program that asks the user for a sentence and then prints the sentence with each word capitalized.
sentence = input("Enter a sentence: ")
capitalized_sentence = sentence.title()
print(f"The sentence with each word capitalized is: {capitalized_sentence}")
