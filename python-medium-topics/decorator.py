"""
-----Decorator is a design pattern and feature \n
-----This allows us to modify or extend the behavior of function main_function without changing main_function code. \n
-----Decorator is a higher-order function because this can take another function/method as argument and return a new
        function that typically enhances/alters the behavior of the original function. \n
-----Use case: \n
----------Logging: Adding logging information before and after a function call. \n
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
--------------------Used to create getter and setter methods for class attributes.
--------------------Add validation or custom behavior when getting or setting an attribute.
--------------------Data Integrity: Prevent invalid values from being assigned to attributes
----------@abstractmethod : from abc import abstractmethod
--------------------Enforcing Method Implementation
--------------------Polymorphism: Using @abstractmethod, we ensure that all concrete subclasses of Animal must provide an implementation of the speak method, maintaining a common interface for polymorphism.
--------------------Like Multiple Payment system follow same payment gateway implementation.
----------@lru_cache : from functools import lru_cache
--------------------is particularly useful for optimizing functions with expensive computations or I/O operations,
                        where results can be reused frequently for the same inputs. It's commonly used for memoization,
                        dynamic programming, and recursive algorithms.
--------------------Very important for cacheing, for same arguments
--------------------This is used to cache the results of function, which help improve the performance of that function, espeically when it's called with the same arguments multiple times.
--------------------Like in fibonacci call @lru_cache can cache the result of `fibonacci(10)` and
                        later if call `fibonacci(20)` be much faster because the function will look up the result in the cache instead of recalculating it.
                        This can significantly improve the performance of that involve expensive calculations.
----------@wraps : from functools import wraps
--------------------`@wraps` decorator is commonly used in conjuction with other decorator to preserve the original
                    function's metadata such as its `name, docstring and parameter information`.
----------@contextmanager : from contextlib import contextmanager
--------------------@contextmanager decorator in Python is used to create context managers,
                        which are helpful for managing resources and setting up and cleaning up a context
                        before and after a block of code is executed. Context managers are commonly used in scenarios
                        where you need to ensure proper resource handling, cleaning up, closing network connections,
                        such as file operations, database connections, locking, and more
----------@asynccontextmanager : from contextlib import asynccontextmanager
----------@dataclass : from dataclasses import dataclass
--------------------This automatically generates an
                        `__init__()`: initialize the object.
                        `__repr__()`: provide a string representation of the object.
                        `__eq__()`: compare instances for equality.
--------------------We can access these methods without having to write them manually.
--------------------Help to reduce boilerplate code
"""

print("----------Basic decorator----------")
from functools import wraps


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
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat_n_times(2)
def greet(name):
    """
        This is a docstring for the greet function.
    """
    print(f"Hello, {name}!")


greet("Alim")

# Accessing metadata of the decorated function
print("Function Name:", greet.__name__)  # Output: "Function Name: greet"
print("Docstring:", greet.__doc__)

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

print("----------Built in decorator @property----------")


class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute with underscore

    @property
    def radius(self):
        """Getter method for the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter method for the radius."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Calculate the area of the circle."""
        return 3.14159 * self._radius ** 2


# Create a Circle object
circle = Circle(5)

# Access the radius using the property
print("Radius:", circle.radius)

# Access the area using the property
print("Area:", circle.area)

# Try to set an invalid radius
# circle.radius = -3  # This will raise a ValueError

print("----------Built in decorator @abstractmethod----------")
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


circle = Circle(5)
print("Circle Area: ", circle.area())
print("Circle Perimeter: ", circle.perimeter())


print("----------Built in decorator Payment Gateway example @abstractmethod----------")


class PaymentGateway(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class PayPal(PaymentGateway):

    def process_payment(self, amount):
        # Implement PayPal-specific payment processing logic here
        print(f"Processing ${amount} via PayPal")


class Stripe(PaymentGateway):

    def process_payment(self, amount):
        # Implement Stripe-specific payment processing logic here
        print(f"Processing ${amount} via Stripe")


print("----------Built in decorator Polymorphism example @abstractmethod----------")


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


print("----------Built in decorator @lru_cache----------")
from functools import lru_cache


# Define a function that computes Fibonacci numbers recursively
# maxsize=None argument means that the cache can grow indefinitely, caching all previously computed results.

'''
The first call to fibonacci(10) computes the 10th Fibonacci number, and the result is cached. 
Subsequent calls to fibonacci(10) or even a larger number like fibonacci(20) will be much faster 
because the function will look up the result in the cache instead of recalculating it. 
This can significantly improve the performance of functions that involve expensive calculations.
'''


@lru_cache(maxsize=None, typed=True)  # The decorator with caching enabled
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Calculate the 10th Fibonacci number
result = fibonacci(10)
print(result)  # Output: 55

# The function has cached the intermediate results, making subsequent calls faster
result = fibonacci(20)
print(result)  # Output: 6765
print("----------Built in decorator @lru_cache complex example 1----------")

# Calculate and print the Fibonacci numbers for various values of n
for n in range(1, 21):
    result = fibonacci(n)
    print(f"Fibonacci 1 ({n}) = {result}")

for n in range(22, 33):
    result = fibonacci(n)
    print(f"Fibonacci 2 ({n}) = {result}")
# Print the cache statistics
print(f"Cache info: {fibonacci.cache_info()}")
fibonacci.cache_clear()
print(f"After Cache info clear: {fibonacci.cache_info()}")

"""
cache_info(hits, misses, maxsize, currsize):
    ~ This cache_info return 4 parameters with the statistics result of the cached function. It's help to understand the behavior and performance of the cached function.
    ~ hits: This represents the number of times a cached result was successfully retrieved from the cache. When a function is called with arguments that have been previously computed and cached, it's considered a "hit" because the function didn't need to recompute the result; instead, it fetched the cached value.
    ~ misses: This represents the number of times the function was called with arguments that were not found in the cache, leading to a recalculation of the result. A "miss" occurs when the function needs to compute a result for arguments that haven't been seen before or when the cache has reached its maximum size and older results need to be removed to make space for new ones.
    ~ maxsize: How much results it will cached. Set `None`, cache will grow indefinitely as new results are cached.
    ~ Typed: Not mandatory parameter. This create separate caches for different argument types.
cache_clear():
    ~ To clear cache result if there is any errors.
Decorator Order: Decorator are applied in the order they are listed. So any caching should be the last step.
Thread Safety: lru_cache is not thread-safe. For thread-safety use third party `cachetools`.
Function Immutability: The function being cached should be 'hashable', meaning it's arguments must be immutable or hashable data types. This is because the cache uses a dictionary to store results and dictionary keys must be hashable.
"""

print("----------Built in decorator @contextmanager----------")

from contextlib import contextmanager, asynccontextmanager
import time


@contextmanager
def timing_context():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.4f} seconds")


# Using the timing_context
with timing_context():
    # Code block for which we want to measure execution time
    for _ in range(1000000):
        pass

# The timing_context will automatically measure and print the time taken
print("----------Built in decorator @contextmanager File I/O----------")


def file_manager(filename, mode):
    file = open(filename, mode)
    yield file
    file.close()


# with file_manager("context_manager.txt", "w") as file:
#     file.write("Context Manager!")
# The file is automatically closed when the block exits.

print("----------Built in decorator @contextmanager Database Connections----------")


import sqlite3


@contextmanager
def database_connection(db_file):
    connection = sqlite3.connect(db_file)
    yield connection
    connection.close()


# with database_connection("pos.db") as conn:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM products")
# The database connection is automatically closed when the block exits.
"""
    Managing database connections and transactions.
    Ensuring that resources are properly released after database operations.
"""

print("----------Built in decorator @contextmanager Locking and Synchronization----------")
import threading

lock = threading.Lock()


@contextmanager
def synchronized():
    lock.acquire()
    try:
        yield
    finally:
        lock.release()


with synchronized():
    # Critical section where only one thread can execute at a time.
    pass
# The lock is automatically released when the block exits.


"""
    Managing locks to control access to shared resources.
    Ensuring that locks are acquired and released correctly.
"""

print("----------Built in decorator @asynccontextmanager----------")

# import asyncio
# import aiofiles
#
#
# # Replace these with your actual resource management functions
# async def acquire_resource(filename):
#     # Open a file for writing asynchronously
#     async with aiofiles.open(filename, mode='w') as file:
#         yield file
#
#
# async def release_resource(file):
#     # Close the file when we're done with it
#     await file.close()
#
#
# @asynccontextmanager
# async def my_async_context_manager(filename):
#     file = await acquire_resource(filename)
#     try:
#         yield file
#     finally:
#         await release_resource(file)
#
# # Usage of the asynchronous context manager
#
#
# async def some_async_function():
#     async with my_async_context_manager("example.txt") as file:
#         await file.write("Hello, world!")
#
# # Ensure to replace acquire_resource and release_resource with your actual resource management functions.
#
# # Run the event loop to execute the async code
# asyncio.run(some_async_function())


print("----------Built in decorator @dataclass----------")
from dataclasses import dataclass, field


@dataclass
class Point:
    x: int
    y: int


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)  # This will print True because the objects have the same attributes.
