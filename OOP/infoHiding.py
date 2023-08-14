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
# class Vehicle:
#     def __init__(self, make, color, model):
#         self.make = make
#         self.color = color
#         self.model = model

#     def printDetails(self):
#         print("Manufacturer:", self.make)
#         print("Color:", self.color)
#         print("Model:", self.model)


# class Car(Vehicle):
#     def __init__(self, make, color, model, doors):
#         # Vehicle.__init__(self, make, color, model)
#         super().__init__(make, color, model)
#         self.doors = doors

#     def printCarDetails(self):
#         self.printDetails()
#         print("Door:", self.doors)


# obj1 = Car("Suzuki", "Grey", "2015", 4)
# obj1.printCarDetails()

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.amount = amount
        self.balance = (self.balance - self.amount)

    def deposit(self, amount):
        self.amount = amount
        self.balance = (self.balance + self.amount)

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return ((self.interestRate * self.balance)/100)


# code to test - do not edit this
demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object
print (demo1.withdrawal)