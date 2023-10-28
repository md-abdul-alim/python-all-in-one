from abc import ABC, abstractmethod


# Define an abstract class using ABC
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Create a concrete subclass of Shape
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Create an instance of the Circle class
circle = Circle(5)

# You can now use the methods defined in the abstract class
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

print("-----------Abstraction method------------")


# Define an abstract class using ABC
class Vehicle(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass


# Create a concrete subclass of Vehicle
class Car(Vehicle):

    def start_engine(self):
        return f"Starting the engine of {self.year} {self.make} {self.model} car."

    def stop_engine(self):
        return f"Stopping the engine of {self.year} {self.make} {self.model} car."

    def accelerate(self):
        return "Car is accelerating."

    def brake(self):
        return "Car is braking."


# Create another concrete subclass of Vehicle
class Motorcycle(Vehicle):

    def start_engine(self):
        return f"Starting the engine of {self.year} {self.make} {self.model} motorcycle."

    def stop_engine(self):
        return f"Stopping the engine of {self.year} {self.make} {self.model} motorcycle."

    def accelerate(self):
        return "Motorcycle is accelerating."

    def brake(self):
        return "Motorcycle is braking."


# Create instances of the Car and Motorcycle classes
car = Car("Toyota", "Camry", 2023)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2023)

# Use the methods defined in the abstract class
print(car.start_engine())
print(car.accelerate())
print(car.brake())
print(car.stop_engine())

print()

print(motorcycle.start_engine())
print(motorcycle.accelerate())
print(motorcycle.brake())
print(motorcycle.stop_engine())

