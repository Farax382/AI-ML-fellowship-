# generators.py

# Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Custom range generator
def my_range(start, end, step=1):
    while start < end:
        yield start
        start += step


if __name__ == "__main__":
    print("Fibonacci:")
    for num in fibonacci(10):
        print(num, end=" ")

    print("\n\nCustom Range:")
    for num in my_range(1, 10, 2):
        print(num, end=" ")
