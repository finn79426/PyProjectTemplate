import functools
import inspect
import time

CYAN = "\033[36m"
RESET = "\033[0m"

def print_input_and_output(func):
    if inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            args_repr = ", ".join(repr(a) for a in args)
            kwargs_repr = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            signature = ", ".join(filter(None, [args_repr, kwargs_repr]))
            print(CYAN + f"IN {func.__name__}({signature})" + RESET)
            result = await func(*args, **kwargs)
            print(CYAN + f"OUT {func.__name__} -> {result!r}" + RESET)
            return result
        return async_wrapper
    else:
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            args_repr = ", ".join(repr(a) for a in args)
            kwargs_repr = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            signature = ", ".join(filter(None, [args_repr, kwargs_repr]))
            print(CYAN + f"IN {func.__name__}({signature})" + RESET)
            result = func(*args, **kwargs)
            print(CYAN + f"OUT {func.__name__} -> {result!r}" + RESET)
            return result
        return sync_wrapper
    
def timeit(func):
    if inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = await func(*args, **kwargs)
            end = time.perf_counter()
            print(CYAN + f"[Async] {func.__name__} executed in {end - start:.6f} seconds" + RESET)
            return result
        return async_wrapper
    else:
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(CYAN + f"[Sync] {func.__name__} executed in {end - start:.6f} seconds" + RESET)
            return result
        return sync_wrapper