from abc import ABC, abstractmethod

# Define an abstract class with an abstract method
class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

# Create concrete subclasses implementing the 'speak' method
class Dog(Animal):

    def speak(self):
        return "Woof!"

class Cat(Animal):

    def speak(self):
        return "Meow!"

class Cow(Animal):

    def speak(self):
        return "Moo!"

# Function that works with any object derived from the Animal class
def make_animal_speak(animal):
    if isinstance(animal, Animal):
        print(f"The animal says: {animal.speak()}")

# Create instances of different animal classes
dog = Dog()
cat = Cat()
cow = Cow()

# Call the function with different animal objects
make_animal_speak(dog)  # Output: "The animal says: Woof!"
make_animal_speak(cat)  # Output: "The animal says: Meow!"
make_animal_speak(cow)  # Output: "The animal says: Moo!"
