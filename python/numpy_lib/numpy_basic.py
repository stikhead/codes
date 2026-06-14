# numpy is a python wrapper around highly optimized c and c++ arrays
# when we create aa numpy array, it allocates a strict, dynamically sized, contigous block of memory
# when an operation is perfored in on a numpy array, python does not run a slow for loop.
# it hands the memory address directly to a compiled c function to perform a "vectorized" operation instantly


import numpy as np

# creating a strict, contiguous array (defaaults to 64 bits floats or ints)
arr = np.array([1, 2, 4, 5, 3, 5])

# vectorized math  (c level speed, no loops)
arr_squared = arr**2

# getting the shape (crucial fro AI to know tensor dimensions)
print(arr.shape) # output: (6, )