import time
def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        start = time.time()
        if args in cache:
            print("fetched from cache")
            end = time.time()
            print(f'time taken: {(end-start)*1000}ms')
            return cache[args]
        else:
            print(f"running {func.__name__}")
            result = func(*args, **kwargs)
            cache[args]  = result
            end = time.time()
            print(f'time taken: {(end-start)*1000}ms')
            return result
    return wrapper

@memoize
def fetch_data(url):
    print("fetching data")
    time.sleep(2)
    print("fetched successfully")
    return "test data"

print(fetch_data("https://codeforces.com/api/id:555"))
print(fetch_data("https://codeforces.com/api/id:555"))