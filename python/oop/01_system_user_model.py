class SystemUser:
    def __init__(self, username, role, rating):
        self.username = username
        self.role = role
        self._rating = rating

    def update_rating(self, points):
        self.rating+=points

    def has_admin_access(self):
        return self.role=="admin"
    
    @property 
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, new_rating):
        if new_rating < 0:
            print("error: rating cannot be negative!")
        else:
            self._rating = new_rating
 
        
    
student = SystemUser("testuser", "student", 1200)
student.update_rating(150)
print(f"{student.rating}")
print(f"admin access: {student.has_admin_access()}")

class AdminUser(SystemUser):
    def __init__(self, username, rating):
        super().__init__(username, "admin", rating)

    def override_rating(self, target_user, new_rating):
        target_user.rating = new_rating


admin = AdminUser("admin",1000)
if(admin.has_admin_access()):
    old_rating = student.rating
    admin.override_rating(student, 1400)
    
    print(f"changed rating from {old_rating} to {student.rating}")

    admin.override_rating(student, -50)