# utils.py

def add_numbers(*args):
    return sum(args)


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


square = lambda x: x * x


def find_max(numbers):
    return max(numbers)


def find_min(numbers):
    return min(numbers)


def find_average(numbers):
    return sum(numbers) / len(numbers)
