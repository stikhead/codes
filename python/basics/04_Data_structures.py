# 1. Lists [] -> equivalent to c++ vectors, they are dynamic can be used to hold mixed types
# 2. Tuples () -> similar to lists but immutable, cannot be changed, fast and efficient
# 3. dictionaries {} -> equivalent to c++ unordered_maps, holds key value pair in sorted ordered
# 4. sets -> equivalent to c++ unorderored_sets, offers fast lookup o(1), unordered collection of unique elements


freq = {}

char = 'x'

freq[char] = freq.get(char, 0) + 1 # get the value's current frequency and add 1 to it if exists other wise use default value and add 1 to it.

day = "yesterday"

# Slicing syntax is [start:stop:step]. A step of -1 reads backwards.
reversed_day = day[::-1]

nums = [1, 2, 3, 4, 5, 6]
# structure: [expression for item in iterable if condition]
even_squares = [x**2 for x in nums if x%2==0] # ** exponential operator
print(even_squares)