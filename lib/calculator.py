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

