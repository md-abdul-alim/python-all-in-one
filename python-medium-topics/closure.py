"""
-----Closure is a concept, like a function define(wrap) another function where the outer function return the inner
    function as result. In closure, first outer function execute the inner function, then the inner function execute
    itself. Here though the outer function already finished the execution, the inner function have the ability to
    access and modify the outer function's variables even after the outer function has finished executing.
-----Closure is to achieve encapsulation (Managing and maintaining state)
-----Decorators are higher-order functions that allow you to modify or extend the behavior of other functions or
    methods without changing their source code. Closures are crucial for implementing decorators.
-----Main function return Closure functions inside Tuple.
------Closure Function use case
----------Decorator
----------Callbacks
----------Managing and maintaining state
----------Functional programming
----------Singleton pattern
----------Creating custom APIs
"""
print("-------------Closure Basic Example 1---------------")
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)
print(result)  # This will print 15
'''
In this example, outer_function takes a parameter x and defines an inner_function that takes a parameter y. 
The inner_function has access to the variable x from its enclosing scope, which is the outer_function. 
When we call outer_function(10), it returns the inner_function as a closure. 
We can then call the closure with closure(5), and it can still access and use the value of x, which was 10 in this case.
'''
print("-------------Closure Decorator Example 2---------------")
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def some_function():
    # Simulate a time-consuming task
    time.sleep(2)

some_function()

print("-------------Closure Callback Example 3---------------")

def perform_operation(x, y, callback):
    result = x + y
    callback(result)

def callback_function(result):
    print(f"The result is: {result}")

perform_operation(10, 5, callback_function)

print("-------------Closure basic 'Managing and maintaining state' Example 4---------------")
def counter():
    count = 0  # Initialize the state

    def increment():
        nonlocal count  # Use 'nonlocal' to indicate we are modifying the outer 'count' variable
        count += 1
        return count  # Return the updated state

    def decrement():
        nonlocal count  # Use 'nonlocal' to indicate we are modifying the outer 'count' variable
        count -= 1
        return count  # Return the updated state

    def get_count():
        return count  # Access the current state

    return increment, decrement, get_count

# Create a counter instance
inc, dec, get = counter()

print("Initial Count:", get())  # Initial Count: 0
print("Incremented:", inc())     # Incremented: 1
print("Incremented:", inc())     # Incremented: 2
print("Decremented:", dec())     # Decremented: 1
print("Current Count:", get())   # Current Count: 1
'''
The 'counter' function returns a tuple of three closures: increment, decrement, and get_count.
NonLocal:
In Python, the nonlocal keyword is used inside a function to indicate that a variable is not local to the function,
but it's also not a global variable. Instead, it's a variable from an outer (enclosing) function's scope. 
In the context of closures, like the example I provided in the previous response, 
the nonlocal keyword is used to inform the function that the variable being referenced or 
modified is in the scope of the enclosing function, not a new local variable.
'''

print("-------------Closure complex 'Managing and maintaining state' Example 5---------------")
def create_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
            return f"Deposited ${amount}. New balance: ${balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(amount):
        nonlocal balance
        if (amount > 0) and (balance >= amount):
            balance -= amount
            return f"Withdrew ${amount}. New balance: ${balance}"
        else:
            return "Invalid withdrawal or insufficient funds."

    def get_balance():
        return f"Available balance ${balance}."

    return deposit, withdraw, get_balance

# Create a bank account
print('Way of calling 1')
account = create_account(1000)

# Perform operations on the account
print(account[0](500))  # Deposited $500. New balance: $1500
print(account[1](200))  # Withdrew $200. New balance: $1300
print(account[2]())     # Current balance: $1300
print(account[1](1500)) # Invalid withdrawal or insufficient funds.

print('Way of calling 2')
deposit, withdraw, get_balance= create_account(1000)
# Perform operations on the account
print(deposit(500))     # Deposited $500. New balance: $1500
print(withdraw(200))    # Withdrew $200. New balance: $1300
print(get_balance())    # Current balance: $1300
print(withdraw(1500))   # Invalid withdrawal or insufficient funds.
'''
This example demonstrates how closures can be used to create a more complex state management system, 
encapsulating the account balance and providing methods to modify and retrieve it. 
The use of closures ensures that the balance variable is not directly accessible or 
modifiable from outside the closures, providing a level of data encapsulation and security.
'''

print("-------------Closure basic 'Functional programming' Example 6---------------")

def filter_list(predicate):
    def apply_filter(lst):
        return [item for item in lst if predicate(item)]

    return apply_filter

# Define a filter function using a closure
filter_even = filter_list(lambda x: x % 2 == 0)
# Define a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use the filter function to filter even numbers
filtered_numbers = filter_even(numbers)
print(filtered_numbers)  # Output: [2, 4, 6, 8, 10]
'''
This is an example of a higher-order function in functional programming. 
It allows you to customize the behavior of the apply_filter function by providing different predicates, 
making it a powerful and flexible tool for data manipulation in a functional style.
'''

print("-------------Closure complex 'Functional programming' (computing compound interest for investments) Example 7---------------")
def compound_interest(principal, rate, time):
    def calculate_amount(p, r, t):
        return p * (1 + r) ** t

    def investment_return():
        return calculate_amount(principal, rate, time) - principal

    return investment_return

# Create a closure to calculate compound interest for an investment
calculate_interest = compound_interest(10000, 0.05, 5)

# Calculate the investment return
interest = calculate_interest()
print(f"Total investment return: ${interest:.2f}")
'''
In this example, we've created a compound_interest function that takes the principal amount, annual interest rate, 
and time (in years) as parameters. It returns a closure investment_return, which calculates the compound interest and 
returns the investment return over the specified time.

When you create a closure using compound_interest with specific values (e.g., $10,000 principal, 5% annual interest, 
and 5 years), it encapsulates these values, allowing you to calculate the investment return by calling the closure.

This is a real-life application of functional programming principles. It uses closures to encapsulate and reuse 
behavior for complex financial calculations, making the code more modular and composable. You can easily create 
multiple closures for different investments with different parameters, promoting code re-usability and maintainability.
'''

print("-------------Closure basic 'Singleton pattern' Example 8---------------")

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class MySingleton:
    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

# Create two instances of MySingleton
singleton_instance1 = MySingleton()
singleton_instance2 = MySingleton()

# Set values in both instances
singleton_instance1.set_value(10)
singleton_instance2.set_value(20)

# Check if both instances share the same value
print(singleton_instance1.get_value())  # Output: 20
print(singleton_instance2.get_value())  # Output: 20

# Check if the instances are the same object
print(singleton_instance1 is singleton_instance2)  # Output: True
'''
In this example, the singleton decorator is created using a closure. It maintains a dictionary called instances 
to store instances of classes as they are created. When you apply the @singleton decorator to the MySingleton class, 
it effectively turns MySingleton into a Singleton. The decorator ensures that only one instance of MySingleton is created and reused.

This is a simple implementation of the Singleton pattern using closures and decorators. It ensures that there is only 
one instance of the MySingleton class, and all requests for that class return the same instance.
'''
print("-------------Closure complex 'Singleton pattern' Example 8---------------")

def singleton_config_manager(config_file_path):
    config = None

    def load_config():
        nonlocal config
        if config is None:
            # Simulate loading configuration from a file
            with open(config_file_path, 'r') as file:
                config = json.load(file)
        return config

    return load_config

# # Create a closure for a Singleton Configuration Manager
# get_config = singleton_config_manager('config.json')
# # Load and use the configuration
# config_data = get_config()
# print("Loaded Configuration Data:", config_data)
# # Try to create another instance (it will still use the same loaded data)
# another_config_data = singleton_config_manager('another_config.json')()
# print("Another Loaded Configuration Data:", another_config_data)
# # Check if both closures share the same configuration data
# print(config_data is another_config_data)  # Output: True

'''
In this example, the singleton_config_manager function is used to create a Singleton Configuration Manager. 
It loads configuration data from a file the first time it's called and caches it. Subsequent calls to get_config 
reuse the cached configuration data. This is a simplified example, but in a real-world scenario, 
the configuration manager might handle more complex configurations, validation, or synchronization.

The Singleton pattern ensures that there's only one instance of the configuration manager, 
making it suitable for managing application settings in a complex application.
'''

print("-------------Closure complex 'Custom API' Example 9---------------")
import hashlib

class UserDatabase:
    def __init__(self):
        self.users = {}  # A dictionary to store user data

    def add_user(self, username, email, password):
        # Perform user data validation
        if not self.is_valid_email(email) or not self.is_valid_password(password):
            return "Invalid email or password format."

        # Hash the password before storing it
        hashed_password = self.hash_password(password)

        # Create a user object and store it in the dictionary
        self.users[username] = {
            "username": username,
            "email": email,
            "password": hashed_password
        }
        return "User added successfully."

    def get_user(self, username):
        return self.users.get(username)

    def clear_database(self):
        self.users = {}

    # Helper methods for validation and password hashing
    def is_valid_email(self, email):
        # Implement email validation logic (e.g., regex)
        return "@" in email

    def is_valid_password(self, password):
        # Implement password validation logic (e.g., length requirements)
        return len(password) >= 8

    def hash_password(self, password):
        # Hash the password before storage (e.g., using hashlib)
        return hashlib.sha256(password.encode()).hexdigest()

# Create a UserDatabase instance
user_db = UserDatabase()

# Add users with complex data and perform validation
print(user_db.add_user("user1", "user1@example.com", "password123"))  # User added successfully.
print(user_db.add_user("user2", "user2example.com", "shortpw"))      # Invalid email or password format.

# Retrieve user information
user_info = user_db.get_user("user1")
print("User Info:", user_info)

# Clear the user database
user_db.clear_database()
user_info = user_db.get_user("user1")
print("Cleared User Info:", user_info)

