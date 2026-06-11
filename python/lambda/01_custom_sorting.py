users = [
    {"name": "Alice", "rating": 1400},
    {"name": "Bob", "rating": 1600},
    {"name": "Charlie", "rating": 1200}
]

users.sort(key=lambda user: user['rating'], reverse=True)
print(users)