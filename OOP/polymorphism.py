# Method overloading
#  some operator methods include:
# Operator	Method
# +	__add__ (self, other)
# -	__sub__ (self, other)
# /	__truediv__ (self, other)
# *	__mul__ (self, other)
# <	__lt__ (self, other)
# >	__gt__ (self, other)
# ==	__eq__ (self, other)

# class Com:
#     def __init__(self, real=0, imag=0):
#         self.real = real
#         self.imag = imag

#     def __add__(self, other):  # overloading the `+` operator
#         temp = Com(self.real + other.real, self.imag + other.imag)
#         return temp

#     def __sub__(self, other):  # overloading the `-` operator
#         temp = Com(self.real - other.real, self.imag - other.imag)
#         return temp


# obj1 = Com(3, 7)
# obj2 = Com(2, 5)

# obj3 = obj1 + obj2
# obj4 = obj1 - obj2

# print("real of obj3:", obj3.real)
# print("imag of obj3:", obj3.imag)
# print("real of obj4:", obj4.real)
# print("imag of obj4:", obj4.imag)

# Animal Class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def Animal_details(self):
        print(self.name)
        print(self.sound)

class Dog(Animal):
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family

    def Animal_details(self):
        print (super().Animal_details())
        print ("Family:", self.family)

class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color
    
    def Animal_details(self):
        print (super().Animal_details())
        print ("Color:", self.color)
    

d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()
print(" ")
s = Sheep("Billy", "Baaa Baaa", "White")
s.Animal_details()

