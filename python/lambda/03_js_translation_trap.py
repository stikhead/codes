# The Scenario: You are migrating an old Node.js microservice to Python (FastAPI). You come across these two JavaScript arrow functions:

# JavaScript
# // Function A
# const getDiscount = price => price > 100 ? price * 0.8 : price;

# // Function B
# const processUser = user => {
#     console.log("Processing:", user.name);
#     return user.rating + 50;
# };

getDiscount = lambda price: price*0.8 if price > 100 else price
print(getDiscount(101))

# no it is not meaningful to convert function b into a lambda func since it contains a body with multiple lines but on the second we could actually do something like this:

user = {
    "name": "a",
    "rating": 50
}
print(f'processing: {user['name']} {(lambda user: user['rating'] + 50)(user)}') 

def process_user(user):
    print("Processing:", user['name'])
    return user['rating'] + 50

# The Test
user = {
    "name": "a",
    "rating": 50
}

# The Execution
new_rating = process_user(user)
print(f"Updated rating: {new_rating}")