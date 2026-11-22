import time
from functools import wraps

def log_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Function Started")
        result = function(*args, **kwargs)
        print("Function Completed")
        return result
    return wrapper

def time_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        print(f"Execution time: {time.perf_counter() - start:.6f} seconds")
        return result
    return wrapper
