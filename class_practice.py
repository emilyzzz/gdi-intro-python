class Vehicle:

    def __init__(self, name="", style="car", color="", value=10000.00):
        self.name = name
        self.style = style
        self.color = color
        self.value = value

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.style, self.value)
        return desc_str


car1 = Vehicle("Fer", "convertible", "red", 60000.00)
car2 = Vehicle("Jump", "van", "blue", 15000.00)


print(car1.description())
print(car2.description())