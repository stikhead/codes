# a lambda function is a small, anonymous function. Unlike a normal function defined with the def keyword, a lambda is created on the fly, typically for a single, short operation.

# standard function:

def add_numbers(x, y):
    return x+y

# lambda function
add = lambda x, y: x + y 
add(2, 4)
add_numbers(2, 4)

# It has no name (unless we assign it to a variable, like add). This is why they are called "anonymous" functions.

# It only contains a single expression, not a block of statements.

# It automatically returns the result of that expression;


# higher order function (a function that takes another function as input)

# 1 sorting complex data:
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)] # list of tuples
people.sort(key=lambda person:person[1])
# Result: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

# 2 using map(), filter
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x:x**2, numbers))
evens = list(filter(lambda x:x%2==0, numbers))
print(evens, squares)

# 3 simple ui callbacks:
import tkinter as tk
button = tk.Button(text="click me", command=lambda: print("button clicked"))

# WHEN LAMBDAS SHOULD BE AVOIDED:
# 1. complex logic: lambda is restricted to a single expression, cannot use loops, try/except blocks, or multi-line if/else statements inside them
# 2. when requires reuse: assigning a lambda to a variable, so it can be used in multiple places, we are defeating the purpose of an anonymous throwaway function.
#  (e.g., calculate_tax = lambda x: x * 0.2) <- use def/regular function instead
# 3. Debugging: when code crashes, the error traceback wull just say the error happened inside <lambda>. if there are multiple lambdas, it can be hard to track down which one failed...

