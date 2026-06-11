import time
def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        
        if args in cache:
            print("fetched from cache")
            return cache['args']
        else:
            print(f"running {func.__name__}")
            cache[args] = func(*args, **kwargs)
            return cache
    return wrapper

@memoize
def fetch_data(url):
    print("fetching data")
    time.sleep(2)
    print("fetched successfully")
    return "test data"

print(fetch_data("https://codeforces.com/api/id:555"))
print(fetch_data("https://codeforces.com/api/id:555"))