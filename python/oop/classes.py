# A Class is the blueprint (e.g., the architectural drawings for a house).
# An Object is the actual thing built from that blueprint (e.g., the physical house you can walk into).
# You can build a hundred houses from one blueprint; they all have the same structure, 
# but different data (different paint colors, different furniture).

# 1. The Blueprint (The Class)
class Robot:
    # This is an empty blueprint
    # pass

# 2. constructor (__init__ and self)
    # The __init__ method is the setup function.
    # 'self' MUST be the first parameter.
    def __init__(self, name, battery_level): # <- basically a constructor (first func that is automatically called when an object is created) 
        self.name = name
        self.battery_level = battery_level
   
    # 4. methods
    def charge_battery(self, amount):
        self.battery_level+=amount
        print(f"{self.name} is now charged to {self.battery_level}")

    def speak(self):
        print(f"hello, im {self.name}")
# 3. instantiating (building the object)
robot_one = Robot("wall-e", 100)
robot_two = Robot("terminator", 80)

print(robot_one.name)
print(robot_two.battery_level)
robot_one.speak()
robot_one.charge_battery(33)
print(robot_one.battery_level)