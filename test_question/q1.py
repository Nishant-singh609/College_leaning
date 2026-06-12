# Q1. Create a class Employee with: (3 Marks) • Private variable __salary = 50000
# • Method increment() → salary += 10000
# • Method deduct() → salary -= 5000
# • Method get_salary() → print salary
# Create 2 objects and call all methods on both.
class Employee:
    def __init__(self):
        self.__salary=50000
    def increment(self):
        self.__salary += 10000
    def deduct(self):
        self.__salary-= 5000
    def get_salary(self):
        print("the total salary=",self.__salary)

print("Employee 1")
E1=Employee()
E1.increment()
E1.deduct()
E1.get_salary()

print("Employee 2\n")

E2=Employee()
E2.increment()
E2.deduct()
E2.get_salary()

