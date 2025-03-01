import random

# Choices list
choices = ['rock', 'paper', 'scissors']

# Start the game loop
while True:
    # Initialize user choice to None for validation loop
    user = None

    # User input validation loop
    while user not in choices:
        user = input("Choose one: rock, paper, scissors: ").lower()
        if user not in choices:
            print("Invalid input. Please choose either rock, paper, or scissors.")

    # Computer randomly chooses rock, paper, or scissors
    computer = random.choice(choices)

    # Display the choices
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")

    # Determine the result
    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        print("You win!")
    else:
        print("You lose!")

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/y/no): ").lower()

    # Exit the game if the user doesn't want to play again
    if play_again not in ['yes', 'y']:
        print("Thanks for playing! Goodbye.")
        break
