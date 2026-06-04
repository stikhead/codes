# Python uses "for-each" loops over iterables.

# Standard loop: 
items = ["8833", "22", "45t"]
for item in items:  # dont use for item in item, it will overwrite the list if list name is item 
    print(item)

# Range loops:
for i in range(5):
    print(i) # provides a range from 0 - 4

# Both index and value loops:
for index, value in enumerate(items): # we always get index first and then value comes after it.  
    print(f'value at {index} is {value}')


names = ["Alice", "Bob", "Charlie"]
for ind, value in enumerate(names, start=1): # we can specify the index to start the loop 
    print(f'{ind} and {value}')