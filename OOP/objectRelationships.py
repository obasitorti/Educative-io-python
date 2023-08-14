# class Country:
#     def __init__(self, name=None, population=0):
#         self.name = name
#         self.population = population

#     def printDetails(self):
#         print("Country Name:", self.name)
#         print("Country Population", self.population)


# class Person:
#     def __init__(self, name, country):
#         self.name = name
#         self.country = country

#     def printDetails(self):
#         print("Person Name:", self.name)
#         self.country.printDetails()


# c = Country("Wales", 1500)
# p = Person("Joe", c)
# p.printDetails()

# # deletes the object p
# del p
# print("")
# c.printDetails()


# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
    
#     def printDetails(self):
#         print("Model:", self.model)
#         print("Color:", self.color)


# class SedanEngine:
#     def __init__(self):
#         pass
    
#     def start(self):
#         print ("Car has started.")

#     def stop(self):
#         print("Car has stopped.")



# class Sedan(Car):
#     def __init__(self, model, color):
#         super().__init__(model, color)
#         self.engine = SedanEngine()

    
#     def setStart(self):
#         self.engine.start()
    
#     def setStop(self):
#         self.engine.stop()
    

# car1 = Sedan("Toyota","Grey")
# car1.setStart()
# car1.printDetails()
# car1.setStop()

