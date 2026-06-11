import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs) # capture actual return value of function
        end = time.time()
        print(f"time taken to execute: {(end-start)*1000}ms")
        return result # return the original result
    return wrapper

@time_it
def heavy_computation():
    sum = 0
    for i in range(10000000):
        for i in range(10):
            pass
        sum+=1
    return sum

result = heavy_computation()
print(result)
