# decorators.py

import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"Execution Time: {end - start:.6f} seconds")
        return result

    return wrapper


@execution_time
def slow_function():
    time.sleep(2)
    print("Function executed")


if __name__ == "__main__":
    slow_function()
