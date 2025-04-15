def calculate(num1, num2, operation):
    """Calculates the result of a simple operation between two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        operation (str): The operation to perform (+, -, *, /).

    Returns:
        int: The result of the calculation.
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero")
            return None
        else:
            return num1 / num2
    else:
        print("Error: Invalid operation")
        return None

def main():
    """Main function for the calculator program."""
    while True:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        result = calculate(num1, num2, operation)
        if result is not None:
            print("Result:", result)
        else:
            print("Calculation failed.")
        if input("Do you want to continue? (y/n): ") == "n":
            break

if __name__ == "__main__":
    main()