class Bike:
    # Class attribute: shared by all instances
    wheels = 2

    # Constructor
    def __init__(self, brand, color):
        # Instance attributes
        self.brand = brand
        self.color = color

    # Instance method
    def display_info(self):
        return f"This {self.color} {self.brand} has {self.wheels} wheels."

# Creating objects (instances)
bike1 = Bike("Yamaha", "black")
bike2 = Bike("Royal Enfield", "green")

# Accessing methods
print(bike1.display_info())
print(bike2.display_info())
