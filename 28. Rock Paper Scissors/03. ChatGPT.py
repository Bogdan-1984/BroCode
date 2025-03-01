import random

def play():
    user = None
    choices = ['rock', 'paper', 'scissors']

    while user not in choices:
        user = input("Choose one: rock, paper, scissors: ").lower()
        if user not in choices:
            print("Invalid input. Please choose either rock, paper, or scissors.")

    computer = random.choice(choices)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You win!"

    return "You lose!"

def is_win(player, opponent):
    # Return True if player beats opponent
    if (player == 'rock' and opponent == 'scissors') or \
       (player == 'scissors' and opponent == 'paper') or \
       (player == 'paper' and opponent == 'rock'):
        return True
    return False

def game_loop():
    while True:
        result = play()
        print(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break

# Run the game
if __name__ == "__main__":
    game_loop()
