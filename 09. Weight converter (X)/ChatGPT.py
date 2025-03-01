"""How to Use:
Follow the prompts to input the weight, the current unit, and the unit you want to convert to.

Explanation:
The convert_weight function uses a dictionary to manage conversion factors between different units.
The main function handles user input and performs the conversion, while also including error handling for 
unsupported units or invalid input.
Feel free to modify the script to add more units or improve the user interface as needed!"""


def convert_weight(weight, from_unit, to_unit):
    # Conversion factors
    conversions = {
        'kg': {'kg': 1, 'g': 1000, 'lb': 2.20462, 'oz': 35.274},
        'g': {'kg': 0.001, 'g': 1, 'lb': 0.00220462, 'oz': 0.035274},
        'lb': {'kg': 0.453592, 'g': 453.592, 'lb': 1, 'oz': 16},
        'oz': {'kg': 0.0283495, 'g': 28.3495, 'lb': 0.0625, 'oz': 1}
    }

    if from_unit not in conversions or to_unit not in conversions[from_unit]:
        raise ValueError("Unsupported unit or conversion")

    return weight * conversions[from_unit][to_unit]


def main():
    print("Welcome to the Weight Converter!")
    print("Available units: kg (kilograms), g (grams), lb (pounds), oz (ounces)")

    try:
        weight = float(input("Enter the weight: "))
        from_unit = input("Enter the current unit (kg/g/lb/oz): ").strip().lower()
        to_unit = input("Enter the unit to convert to (kg/g/lb/oz): ").strip().lower()

        result = convert_weight(weight, from_unit, to_unit)
        print(f"{weight} {from_unit} is equal to {result:.4f} {to_unit}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
