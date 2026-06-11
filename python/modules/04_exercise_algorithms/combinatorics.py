from collections import Counter
from itertools import combinations, accumulate
import math 
ratings = [1200, 1400, 1200, 1500, 1400, 1200, 1600]
max_unique_rating = 0
second_max_unique_rating = 0
freq = Counter(ratings)
for item, frequency in freq.items():
    if frequency==1 and item>=max_unique_rating:
        second_max_unique_rating = max_unique_rating
        max_unique_rating = item

    print(f'{item}: {frequency}')

combi = list(combinations(list(freq.keys()), 2))
length = list(accumulate(combi))
print(combi)
print(len(combi))
print(length)

highest, second_highest = sorted(list(freq.keys()), reverse=True)[:2]
gcd_rates = math.gcd(highest, second_highest)
gcd_ratings = math.gcd(max_unique_rating, second_max_unique_rating)
print(max_unique_rating, second_max_unique_rating)
print(gcd_ratings)
