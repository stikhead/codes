# global dictionary simulating an active user session: 
import random

current_user = {}
rndval = random.randint(0, 1)
if rndval: 
    current_user['username'] = "admin_user"
    current_user["role"] = "admin"
    
else:
    current_user['username'] = "student_user"
    current_user["role"] = "student"

def requires_admin(func):
    def wrapper(*args, **kwargs):
        if current_user['role'] == "admin":
            return func(*args, **kwargs)
        else:
            raise PermissionError("HTTP 403: Forbidden")
    return wrapper

@requires_admin
def delete_database():
    print("deleting database...")
    return random.randint(0, 1)

result = delete_database()
if result:
    print('deleted successfully')
elif result == 0: 
    print("an error occurred")

