import random

# print(help(random)) = full list of what module can do

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ("2", "3", "4", "5", "6", "7", "8", "Q", "K", "A", )
card_list = list(cards)

# option 1 = number = random.randint(1, 20)
# option 2 = number = random.randint(low, high)

# number = random.random()

# option = random.choice(options)

random.shuffle(card_list)

print(card_list )