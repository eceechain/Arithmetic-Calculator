# Function to perform addition of two numbers
def add(x, y):
    return x + y

# Function to perform subtraction of two numbers
def subtract(x, y):
    return x - y

# Function to perform multiplication of two numbers
def multiply(x, y):
    return x * y

# Function to perform division of two numbers
def divide(x, y):
    # Check if the divisor is zero to avoid division by zero error
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to perform modulo operation of two numbers
def modulo(x, y):
    # Check if the divisor is zero to avoid modulo by zero error
    if y == 0:
        return "Error! Modulo by zero."
    return x % y

# Main calculator function
def calculator():
    while True:
        # Display options for the user to select an operation
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")
        print("6. Exit")

        # Take user input for operation choice
        choice = input("Enter choice (1/2/3/4/5/6): ")

        # Perform the selected operation based on user input
        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))  # Take the first number as input
            num2 = float(input("Enter second number: "))  # Take the second number as input

            # Perform the selected operation and display the result
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", modulo(num1, num2))
        elif choice == '6':
            print("Exiting the calculator. Goodbye!")
            break  # Exit the calculator loop
        else:
            print("Invalid Input")  # Display error message for invalid input

# Run the calculator function when the script is executed directly
if __name__ == "__main__":
    calculator()
