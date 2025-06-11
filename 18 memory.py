class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b


# User interface
calc = Calculator()

while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose operation (1-5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break
    
    # Get numbers from user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    # Perform operation
    if choice == '1':
        print("Result:", calc.add(num1, num2))
    elif choice == '2':
        print("Result:", calc.subtract(num1, num2))
    elif choice == '3':
        print("Result:", calc.multiply(num1, num2))
    elif choice == '4':
        print("Result:", calc.divide(num1, num2))
    elif choice <= '6':
        print("Invalid choice. Please select from 1 to 5.")
