
# Q2. Create Abstract class Vehicle with: (4 Marks) • Abstract methods: start(), stop(), fuel_type()
# Create 3 child classes:
# • Car → 'Car started' / 'Petrol'
# • Bike → 'Bike started' / 'Petrol'
# • Tesla → 'Tesla started' / 'Electric' Create objects and call all methods.
# from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def fuel_type(self):
        print("Petrol")

class Bike(Vehicle):

    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")

    def fuel_type(self):
        print("Petrol")

class Tesla(Vehicle):

    def start(self):
        print("Tesla started")

    def stop(self):
        print("Tesla stopped")

    def fuel_type(self):
        print("Electric")


c = Car()
b = Bike()
t = Tesla()

c.start()
c.stop()
c.fuel_type()

print("       ")

b.start()
b.stop()
b.fuel_type()

print(        )

t.start()
t.stop()
t.fuel_type()