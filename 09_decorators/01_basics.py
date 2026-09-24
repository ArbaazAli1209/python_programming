from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator

def greet():
    print("Hello from decorators class from chaicode")

greet()
print(greet.__name__)  # Output: wrapper