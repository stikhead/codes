# At its core, a decorator is just a function that takes another function as an argument, 
# adds some extra behavior to it, and returns it.

# step 1: manual way
# def log_action(func): # decorator
#     def wrapper():
#         print(f"starting: {func.__name__}")
#         func() # orignal func exectuion
#         print(f"finshed: {func.__name__}")
#     return wrapper


# def sync_datebase(): # orginal function
#     print("connecting to db... synced!")

# sync_datebase = log_action(sync_datebase) # manual wrapping 

# sync_datebase()

# step 2: pythonic @ syntax
def log_action(func):
    def wrapper():
        print(f"STARTING: {func.__name__}")
        func() 
        print(f"FINISHED: {func.__name__}")
    return wrapper

@log_action
def sync_database():
    print("connecting to db...")

sync_database()

# step 3: real world devops/backend example
# When building backend systems or automated tools (like scraping contest schedules), 
# network requests fail all the time.
# Instead of writing try/except and sleep logic inside every single function, 
# engineers write a @retry decorator.

import time

def retry_on_fail(func):
    def wrapper(*args, **kwargs):
        attempts = 3
        for i in range(attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"attempt {i+1} failed: {e}. Retrying...")
                time.sleep(1)
        print("all retries failed")
    return wrapper

@retry_on_fail
def fetch_platform_data(url):
    import random
    if random.random() < 0.7:
        raise ConnectionError("timeout!")
    return f"data from {url} fetched"

result = fetch_platform_data("https://codeforces.com/api/contests")
print(result)