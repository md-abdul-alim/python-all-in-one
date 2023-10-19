
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
# Define a decorator function
def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello before the function is called!")
        result = func(*args, **kwargs)
        print("Hello after the function is called!")
        return result
    return wrapper

# Apply the decorator to a function using the "@" symbol
@greeting_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Call the decorated function
say_hello("Alice")
