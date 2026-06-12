# "
# Q3. Create a Hybrid Inheritance program: (3 Marks) • Father: property(), business()
# • Son(Father): study()
# • Daughter(Father): dance()
# • GrandChild(Son, Daughter): gaming()
# Create object of GrandChild and call ALL methods.
# "
class Father:
    def property(self):
        print("Father a car,bus,land,house")
    
    def business(self):
        print("father has a business ,this property in feature mine")
class Son(Father):
    def study(self):
        print("i am doing b.tech")
class Daughter(Father):
    def dance(self):
        print("sister is learning dance")
class GrandChild(Son, Daughter):
    def gaming(self):
        print("Son,Daughter plays game with the GrandChild")


G1=GrandChild()
G1.business()
print()
G1.dance
print()
print()
G1.gaming
print()
print()
G1.property
print()
G1.study
print()
print()
        