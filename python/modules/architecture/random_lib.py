import random

print(random.randint(1, 10)) # random int betweem 1 and 10 (inclusive)
print(random.choice(['A', 'B', 'C'])) # pick a random element

deck = [1, 2, 3, 4, 5]
random.shuffle(deck) # shuffles the list in place
print(deck)