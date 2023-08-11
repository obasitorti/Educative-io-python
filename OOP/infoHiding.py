# # # Getting and setting methods

# # class User:
# #     def __init__(self, username=None):
# #         self.__username = username
    
# #     def setUsername(self, x):
# #         self.__username = x

# #     def getUsername(self):
# #         return (self.__username)

# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width

#     def area(self):
#         return (self.__length * self.__width)

#     def perimeter(self):
#         return (2*(self.__length + self.__width))
    
# Rectangle1 = Rectangle(4, 5)

# print(Rectangle1.perimeter)

# Inheritance
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # Vehicle.__init__(self, make, color, model)
        super().__init__(make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Door:", self.doors)


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()