while True:
    try:
        # Prompt the user to enter their age
        age = int(input("Enter your age: "))

        # Check the age and provide the appropriate response
        if age >= 100:
            print("You are too old to sign up.")
        elif age >= 18:
            print("You are now signed up.")
            break  # Exit the loop since valid input has been processed
        elif age < 0:
            print("You haven't been born yet.")
        else:
            print("You must be 18+ to sign up.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
