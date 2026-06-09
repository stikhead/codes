# Memory-safe iterators for brute-force algorithms and math logic.

from itertools import permutations, combinations
items = ['A', 'B', 'C']
print(list(permutations(items, 3)))
print(list(combinations(items, 3)))

from itertools import accumulate
arr = [1, 4, 3, 2, 3, 4]
sum = list(accumulate(arr))
print(sum)

