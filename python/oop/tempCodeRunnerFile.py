def rate_limit(func):
    call_count = 0
    def wrapper(*args, **kwargs):
        nonlocal call_count
        if call_count < 3:
            call_count+=1
            return func(*args, **kwargs)
        else:
            raise ConnectionRefusedError("HTTP 429: Too Many Requests")
        
    return wrapper

@rate_limit
def fetch_data(url):
    return "success"

for i in range(4):
    print(fetch_data("https://"))