"Function with parameters and a return value"


def greet(name, age):
    """
    This function greets the user with their name and age.
    """
    return f"Hello, {name}! You are {age} years old."

# Function with default arguments


def greet_with_default(name, age=25):
    """
    This function greets the user with their name and age.
    If no age is provided, it defaults to 25.
    """
    return f"Hello, {name}! You are {age} years old."

# Function with variable-length arguments (using *args)


def sum_numbers(*args):
    """
    This function takes any number of arguments and returns their sum.
    """
    return sum(args)

# Function with variable-length keyword arguments (using **kwargs)


def describe_person(name, **kwargs):
    """
    This function describes a person. It takes a name and any number of additional keyword arguments.
    """
    description = f"Name: {name}\n"
    for key, value in kwargs.items():
        description += f"{key}: {value}\n"
    return description


# Lambda function (anonymous function)
def multiply(x, y): return x * y

# Nested function


def outer_function(x):
    """
    This function demonstrates a function containing another function.
    """
    def inner_function(y):
        return y + 2
    return inner_function(x)

# Higher-order function (a function that takes another function as an argument)


def apply_function(func, value):
    """
    This function takes another function and applies it to a value.
    """
    return func(value)

# Decorator function (used to modify the behavior of another function)


def decorator(func):
    """
    A simple decorator that modifies the behavior of the function by printing additional info before and after the function is executed.
    """
    def wrapper(*args, **kwargs):
        print("Function execution started")
        result = func(*args, **kwargs)
        print("Function execution ended")
        return result
    return wrapper

# Applying a decorator


@decorator
def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the result.
    """
    return a * b

# Recursive function


def factorial(n):
    """
    This function calculates the factorial of a number recursively.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example of using the functions above:


# 1. Calling a function with parameters and return value
name = "Alice"
age = 30
greeting = greet(name, age)
print(greeting)  # Output: Hello, Alice! You are 30 years old.

# 2. Calling a function with default arguments
default_greeting = greet_with_default("Bob")
print(default_greeting)  # Output: Hello, Bob! You are 25 years old.

# 3. Calling a function with variable-length arguments
result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15

# 4. Calling a function with variable-length keyword arguments
description = describe_person("Charlie", occupation="Engineer", location="NYC")
print(description)
# Output:
# Name: Charlie
# occupation: Engineer
# location: NYC

# 5. Calling a lambda function
product = multiply(3, 4)
print(product)  # Output: 12

# 6. Calling a nested function
outer_result = outer_function(5)
print(outer_result)  # Output: 7 (inner function adds 2 to the passed value)

# 7. Using a higher-order function
squared = apply_function(lambda x: x ** 2, 4)
print(squared)  # Output: 16 (applies the lambda function that squares the value)

# 8. Using a decorated function
result = multiply_numbers(3, 5)
print(result)  # Output: Function execution started \n Function execution ended \n 15

# 9. Calling a recursive function
fact = factorial(5)
print(fact)  # Output: 120 (5! = 5 * 4 * 3 * 2 * 1)
