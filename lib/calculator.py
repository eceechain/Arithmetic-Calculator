def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error!!"
    while True:
     #menu
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        # Get user input
    
choice = input("Enter choice (1/2/3/4/5): ")

    # Check if the user wants to exit
if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break  # Exit the loop

# Perform the operation based on user's input
 # Check if the choice is valid
if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the selected operation
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        