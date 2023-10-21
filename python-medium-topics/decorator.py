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
----------@property
----------@abstractmethod : from abc import abstractmethod
----------@lru_cache : from functools import lru_cache
----------@wraps : from functools import wraps
----------@contextmanager : from contextlib import contextmanager
----------@asynccontextmanager : from contextlib import asynccontextmanager
----------@dataclass : from dataclasses import dataclass
"""


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
