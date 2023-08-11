class Employee:
    # defining the properties and assigning them None
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return (self.salary * 0.2)
    
    def salaryPerDay(self):
        return (self.salary / 30)

    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)


Steve = Employee()

print("Demo 1")
Steve.demo(1, 2, 3, 4)
# # creating an object of the Employee class with default parameters
# Steve = Employee(3789, 2500, "Human Resources")

# # Printing properties of Steve
# print("ID :", Steve.ID)
# print("Salary :", Steve.salary)
# print("Department :", Steve.department)
# print("Taxes paid by Steve:", Steve.tax())
# print("Salary per day of Steve", Steve.salaryPerDay())