# 1. private convention:
# Python doesn't have a strict private keyword. 
# Instead, we use an underscore _ to tell other developers,
# "Hey, this is an internal variable, do not touch it directly."

# 2. getters (@property):
# we wrap a method that returns the internal variables

# 3. setter (@name.setter)
# we wrap a method that validates the data before saving it

class Thermostat:
    def __init__(self, temperature):
        # soring actual data in a private variable using _
        self._temperature = temperature

    # the getter: this lets us read bot.temperature without parantheses
    @property
    def temperature(self):
        return self._temperature
    
    # the setter: this intercepts 'bot.temperature = x'
    @temperature.setter
    def temperature(self, value):
        if value < -273:
            print("invalid value, cannot go below absolute zero!")
        else:
            self._temperature = value


office = Thermostat(20)
# calls the @property getter
print(office.temperature)

# calls the @temperature.setter
office.temperature = -500 # output: invalid value, cannot go below absolute zero!