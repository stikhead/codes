# inheritane lets use to create a child class that absorbs all methods and variable of a parent class
class SystemUser:
    def __init__(self, username, role, rating):
        self.username = username
        self.role = role
        self.rating = rating

    def update_rating(self, points):
        self.rating+=points

    def has_admin_access(self):
        return self.role=="admin"
        
# pass the parent class into the parentheses
class AdminUser(SystemUser):

    # we still need an init for the child if we want to add new data
    def __init__(self, username, rating, privileges):
        # super() calls the parent's __init__ so we dont have to rewrite it
        super().__init__(username, "admin", rating)

        # then we add admin specific data (child specific data)
        self.privileges = privileges


# Because AdminUser inherits from SystemUser, any object created from AdminUser
#  automatically has access to .update_rating() and .has_admin_access()
student = SystemUser("testuser", "student", 1200)
admin = AdminUser("admin", 1000, "all_access")
admin.update_rating(100)
print(admin.rating)
student.update_rating(150)
print(f"{student.rating}")
print(f"admin access: {student.has_admin_access()}")

