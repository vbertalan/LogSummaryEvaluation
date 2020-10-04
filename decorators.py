import functools


# Borrowed from https://realpython.com/primer-on-python-decorators/
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug


def print_step(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_print_name(*args, **kwargs):
        print(f"Calling {func.__qualname__}")
        value = func(*args, **kwargs)
        return value
    return wrapper_print_name
