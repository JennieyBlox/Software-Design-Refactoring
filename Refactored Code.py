class Calculator:
    """A simple calculator class."""

    def add(self, num1, num2):
        """Adds two numbers."""
        return num1 + num2

    def subtract(self, num1, num2):
        """Subtracts two numbers."""
        return num1 - num2

    def multiply(self, num1, num2):
        """Multiplies two numbers."""
        return num1 * num2

    def divide(self, num1, num2):
        """Divides two numbers."""
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2

def main():
    """Main function for the calculator program."""
    calculator = Calculator()
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == "+":
                result = calculator.add(num1, num2)
            elif operation == "-":
                result = calculator.subtract(num1, num2)
            elif operation == "*":
                result = calculator.multiply(num1, num2)
            elif operation == "/":
                result = calculator.divide(num1, num2)
            else:
                raise ValueError("Invalid operation")

            print("Result:", result)

        except (ZeroDivisionError, ValueError) as e:
            print("Error:", e)

        if input("Do you want to continue? (y/n): ") == "n":
            break

if __name__ == "__main__":
    main()