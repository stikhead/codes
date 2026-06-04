import random


def get_matrices(nums):
    min = 10000000000000
    max = 0
    for num in nums:
        if num <= min:
            min = num
        elif num >= max:
            max = num
    return min, max 
    # return min(nums), max(nums)

nums = [3, 4,2, 45,6 ,53]
lowest, highest = get_matrices(nums)
print(get_matrices(nums))

# Never use an empty list [] or dictionary {} as a default argument in Python
# default arguements are created exaqctly once in python. if we were to add items in list inside this function,
# that same list would stay modified in memory for every subsequent time you called the function!
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

# First pass
print(add_item(1))  
# Output: [1]

# Second pass
print(add_item(2))  
# Output: [1, 2]

# Third pass
print(add_item(3))  
# Output: [1, 2, 3]


# Industry standard:
def add_item_safely(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list


# flexible arguments in function (args, kwargs)
def log_event(*args, **kwrgs):
    print("Codes:", args)
    print("errors:", kwrgs)

log_event(404, user="admin", ip="10.0.0.1")


def port_config(port_str):
    try:
        return int(port_str)
    except ValueError: # catching specific errors to avoid masking any unrelated errors
        return 80

port = port_config("8080d")
print(port)

def connect_to_db():
    val = random.randint(0, 1)
    if val:
        return True
    else:
        raise ConnectionError("Database timeout or refused connection.")
    
def connection():
    try:
        db_success = connect_to_db()
    except ConnectionError as e:
        print("failed", {e})
    else:
        print("success", db_success)
    finally:
        print("closing cleanup")


connection()

    