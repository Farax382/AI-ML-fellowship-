# exception_handling.py

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Choose operation (+ - * /): ")

    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operation")

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Calculation successful.")

finally:
    print("Program finished.")
