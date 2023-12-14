# calculator.py
import math
from models import CalculationHistory, session

def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /, sin, cos, tan, log): ")
        return num1, num2, operation
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_user_input()

def perform_arithmetic_operation(num1, num2, operation):
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero.")
                return None
            result = num1 / num2
        elif operation == "sin":
            result = math.sin(math.radians(num1))
        elif operation == "cos":
            result = math.cos(math.radians(num1))
        elif operation == "tan":
            result = math.tan(math.radians(num1))
        elif operation == "log":
            if num1 <= 0:
                print("Error: Invalid input for log base 10.")
                return None
            result = math.log10(num1)
        else:
            print("Invalid operation. Please enter +, -, *, /, sin, cos, tan, or log.")
            return None

        return result
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None

def display_result(result):
    if result is not None:
        print("Result:", result)

def main():
    result = None
    memory = None

    while True:
        print("\n=== Calculator Menu ===")
        print("1. Perform Calculation")
        print("2. Clear Result")
        print("3. Memory Recall")
        print("4. Memory Clear")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            num1, num2, operation = get_user_input()
            result = perform_arithmetic_operation(num1, num2, operation)
            display_result(result)
            if result is not None:
                # Store the calculation in the database
                calculation_history = CalculationHistory(expression=f"{num1} {operation} {num2}", result=str(result))
                session.add(calculation_history)
                session.commit()
        elif choice == "2":
            print("Result cleared.")
            result = None
        elif choice == "3":
            if memory is not None:
                print("Memory Recall:", memory)
                result = memory
            else:
                print("Memory is empty.")
        elif choice == "4":
            print("Memory cleared.")
            memory = None
        elif choice == "5":
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
