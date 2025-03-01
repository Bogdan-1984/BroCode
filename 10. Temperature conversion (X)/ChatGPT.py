"""How it Works:
Conversion Functions: Each function converts temperatures between different units.
print_menu(): Displays the available conversion options to the user.
main(): The main loop that interacts with the user, reads their choice, and performs the appropriate conversion.
Usage:
Run the script.
Select the conversion type by entering the corresponding number.
Input the temperature value when prompted.
View the result.
Choose to exit by entering 7."""


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def print_menu():
    print("Temperature Conversion Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Exiting...")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            temp = float(input("Enter the temperature value: "))

        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp} Celsius is {result:.2f} Fahrenheit.")
        elif choice == '2':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp} Fahrenheit is {result:.2f} Celsius.")
        elif choice == '3':
            result = celsius_to_kelvin(temp)
            print(f"{temp} Celsius is {result:.2f} Kelvin.")
        elif choice == '4':
            result = kelvin_to_celsius(temp)
            print(f"{temp} Kelvin is {result:.2f} Celsius.")
        elif choice == '5':
            result = fahrenheit_to_kelvin(temp)
            print(f"{temp} Fahrenheit is {result:.2f} Kelvin.")
        elif choice == '6':
            result = kelvin_to_fahrenheit(temp)
            print(f"{temp} Kelvin is {result:.2f} Fahrenheit.")
        else:
            print("Invalid choice. Please select a number between 1 and 7.")


if __name__ == "__main__":
    main()
