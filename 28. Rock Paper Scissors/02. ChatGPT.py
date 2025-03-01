import random

def play():
    user = input("Choose one: rock, paper, scissors: ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You win!"

    return "You lose!"

def is_win(player, opponent):
    # Return True if player beats opponent
    # Winning combinations: rock beats scissors, scissors beat paper, paper beats rock
    if (player == 'rock' and opponent == 'scissors') or \
       (player == 'scissors' and opponent == 'paper') or \
       (player == 'paper' and opponent == 'rock'):
        return True
    return False

# Run the game
if __name__ == "__main__":
    print(play())
