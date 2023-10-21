"""
-----Decorator is a design pattern and feature
-----This allows us to modify or extend the behavior of function main_function without changing main_function code.
-----Decorator is a higher-order function because this can take another function/method as argument and return a new
        function that typically enhances/alters the behavior of the original function.
-----Use case:
----------Logging: Adding logging information before and after a function call.
----------Authentication and Authorization: Checking user permissions or authentication status before allowing access.
----------Timing and Profiling: Measuring the execution time of functions.
----------Caching: Storing the result of function calls to improve performance.
----------Route Handling: Directing HTTP requests to the appropriate functions
-----Built-in decorators:
----------@staticmethod
--------------------Doesn't have access to instance-specific data (attributes). Static method can't access self.
--------------------It can only access and manipulate data that is passed as arguments or is defined within the method itself
--------------------Static method is directly associated with the class not with the instance.
--------------------Static method can call both directly by Class and class instance. But typically calling by class itself to make it more clear that they don't rely on instance-specific data.
--------------------Non-static method technically possible to call directly by Class. But in this case we must pass
                        (self/instance) as first parameter. Which is not a recommended practice.
--------------------Non-static method is not directly associated with class.
--------------------Non-static method is only accessible by class instance.
--------------------Non-static method can access class attributes using self.
--------------------Note:
--------------------~ Static method makes it explicit that a method is designed to used in class-wide context,
                            which can help prevent accidental use in an instance-specific context.
----------@classmethod
--------------------Class method can share its own attributes data among all the instances of the class, which can be
                        modified and accessed via the class method
--------------------Class method as Alternative Constructor: example bellow
--------------------Access or modify class-level attributes: example bellow
--------------------Factory Methods: allows to create class instance with additional logic, validation or data manipulation
--------------------Singleton Pattern: Implement the Singleton patter, to ensuring that a class has only one instance throughout the program.
--------------------Caching and Memoization
--------------------Database Connection Pooling: It involves dealing with database connections , thread safety, and resource management.
--------------------Creating Helper Function
----------@property
----------@abstractmethod : from abc import abstractmethod
----------@lru_cache : from functools import lru_cache
----------@wraps : from functools import wraps
----------@contextmanager : from contextlib import contextmanager
----------@asynccontextmanager : from contextlib import asynccontextmanager
----------@dataclass : from dataclasses import dataclass
"""

print("----------Basic decorator----------")


def greeting_decorator(main_function):
    def main_function_wrapper(*args, **kwargs):
        print("Hello before the function is called!")
        result = main_function(*args, **kwargs)
        print("Hello after the function is called!")
        return result
    return main_function_wrapper


@greeting_decorator
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Md. Abdul Alim")


#  Decorator using higher order function
print("----------Decorator with higher order function----------")


def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat_n_times(2)
def greet(name):
    print(f"Hello, {name}!")


greet("Alim")

# repeat_n_times(3)(greet)('Milon')
'''
repeat_n_times()
greet()
Note:
    ~ Here `repeat_n_times` is a higher-order function
'''


#  @staticmethod
print("----------Built in decorator @staticmethod----------")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_area_non_static_call_test(self, height):
        return self.length * self.width * height

    @staticmethod
    def calculate_area_static(length, width):
        return length * width


# Create an instance of the Rectangle class
rect_instance = Rectangle(5, 3)

# Call the instance method to calculate the area
area_instance = rect_instance.calculate_area()
print(f"Area using instance method: {area_instance}")

# Call the static method to calculate the area
area_static = Rectangle.calculate_area_static(length=4, width=2)
print(f"Area using static method: {area_static}")

# Call non-static method directly by Class. Which is not a recommended practice
area_non_static = Rectangle.calculate_area_non_static_call_test(rect_instance, 2)
print(f"Area using non-static method by directly Class call: {area_non_static}")

print("----------Built in decorator @staticmethod ~~~ Date Validation using @staticmethod----------")


class DateUtils:
    @staticmethod
    def is_valid_date(year, month, day):
        try:
            from datetime import datetime
            datetime(year, month, day)
            return True
        except ValueError:
            return False

# Using the static method to validate a date
year = 2023
month = 2
day = 29

if DateUtils.is_valid_date(year, month, day):
    print(f"{year}-{month}-{day} is a valid date.")
else:
    print(f"{year}-{month}-{day} is not a valid date.")


#  @classmethod
print("----------Built in decorator @classmethod----------")


class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value

    @classmethod
    def class_method(cls):
        cls.class_variable += 1
        print(f"This is a class method. Class variable is now {cls.class_variable}")


# Creating instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)

# Calling the class method on the class itself
MyClass.class_method()  # Output: This is a class method. Class variable is now 1

# Accessing class variables
print(f"Class variable from obj1: {obj1.class_variable}")
print(f"Class variable from obj2: {obj2.class_variable}")

# You can also call the class method on an instance (not common)
obj1.class_method()  # Output: This is a class method. Class variable is now 2

# Accessing class variables after calling the class method
print(f"Class variable from obj1: {obj1.class_variable}")
print(f"Class variable from obj2: {obj2.class_variable}")

print("----------Built in decorator @classmethod ~~~ create alternative constractor using @classmethod----------")


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        first_name, last_name = full_name.split()
        return cls(first_name, last_name)

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")


# Creating instances using the regular constructor
person1 = Person("Abdul", "Alim")
person1.display_info()

# Creating an instance using the class method
person2 = Person.from_full_name("Esrat Jahan")
person2.display_info()


print("--------Built in decorator @classmethod ~~~ Access or modify class level attribute using @classmethod--------")


class Car:
    total_cars = 0  # Class-level attribute to keep track of the total number of cars

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1  # Increment the class-level attribute

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

    @classmethod
    def reset_total_cars(cls):
        cls.total_cars = 0


# Create instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")
car3 = Car("Ford", "Mustang")

# Access the total number of cars using the class method
total_cars = Car.get_total_cars()
print(f"Total number of cars: {total_cars}")

# Reset the total number of cars using the class method
Car.reset_total_cars()

# Check the total number of cars again
total_cars = Car.get_total_cars()
print(f"Total number of cars after reset: {total_cars}")


print("--------Built in decorator @classmethod ~~~ Factory method using @classmethod--------")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def create_product_with_discount(cls, name, price, discount_percentage):
        # Additional logic to calculate the discounted price
        discounted_price = price - (price * discount_percentage / 100)
        return cls(name, discounted_price)

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Original Price: ${self.price:.2f}")


# Creating instances of the Product class using the customized factory method
product1 = Product.create_product_with_discount("Laptop", 999.99, 10)  # 10% discount
product2 = Product.create_product_with_discount("Headphones", 49.99, 20)  # 20% discount

# Display product information
product1.display_info()
product2.display_info()

print("--------Built in decorator @classmethod ~~~ Singleton Pattern using @classmethod--------")


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

instance1 = Singleton()
instance2 = Singleton()

print(instance1 is instance2) # This will be True

print("--------Built in decorator @classmethod ~~~ Caching and Memoization using @classmethod--------")


class MathOperations:
    _cache = {}

    @classmethod
    def square(cls, num):
        if num not in cls._cache:
            print(f'Print num once: {num}')
            result = num * num
            cls._cache[num] = result
        return cls._cache

print(MathOperations.square(4)) # Calculates and caches 16
print(MathOperations.square(4)) # Returns cached result 16

print("--------Built in decorator @classmethod ~~~ Database Connection Pooling using @classmethod--------")


import threading

class DatabaseConnectionPool:
    _connection_pool = []
    _max_connections = 5
    _lock = threading.Lock()

    @classmethod
    def get_connection(cls):
        # A lock is used to ensure thread safety
        with cls._lock:
            if not cls._connection_pool:
                if len(cls._connection_pool) < cls._max_connections:
                    # Simulate creating a new database connection
                    connection = f"Connection{len(cls._connection_pool) + 1}"
                    cls._connection_pool.append(connection)
                    print(f"Created a new connection: {connection}")
                else:
                    print("Connection limit reached. Waiting for a connection to become available.")
                    cls._lock.release()
                    # Simulate waiting for a connection to become available
                    while not cls._connection_pool:
                        pass
                    cls._lock.acquire()

            # Simulate returning a database connection from the pool
            connection = cls._connection_pool.pop()
            print(f"Got a connection: {connection}")
            return connection

    @classmethod
    def release_connection(cls, connection):
        with cls._lock:
            # Simulate releasing a connection back to the pool
            cls._connection_pool.append(connection)
            print(f"Released connection: {connection}")

# Simulate multiple threads requesting and releasing connections
def simulate_database_operations():
    for _ in range(3):
        connection = DatabaseConnectionPool.get_connection()
        # Simulate performing database operations
        DatabaseConnectionPool.release_connection(connection)

threads = []
for _ in range(3):
    thread = threading.Thread(target=simulate_database_operations)
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("--------Built in decorator @classmethod ~~~ Create Helper Function using @classmethod--------")


class StringUtils:
    @classmethod
    def reverse_string(cls, text):
        return text[::-1]

    @classmethod
    def count_vowels(cls, text):
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)

    @classmethod
    def is_palindrome(cls, text):
        cleaned_text = ''.join(filter(str.isalnum, text)).lower()
        return cleaned_text == cleaned_text[::-1]

# Using the class methods to perform string operations
text1 = "hello world"
reversed_text = StringUtils.reverse_string(text1)
vowel_count = StringUtils.count_vowels(text1)
is_palindrome = StringUtils.is_palindrome("A man, a plan, a canal, Panama")

print(f"Original Text: {text1}")
print(f"Reversed Text: {reversed_text}")
print(f"Vowel Count: {vowel_count}")
print(f"Is Palindrome: {is_palindrome}")
