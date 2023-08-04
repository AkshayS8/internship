def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def calculator():
    print("Welcome to Simple Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (0-4): "))

            if choice == 0:
                print("Thank you for using Simple Calculator!")
                break

            if choice not in range(1, 5):
                print("Invalid choice. Please enter a valid option (0-4).")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print("Result:", add(num1, num2))
            elif choice == 2:
                print("Result:", subtract(num1, num2))
            elif choice == 3:
                print("Result:", multiply(num1, num2))
            elif choice == 4:
                try:
                    print("Result:", divide(num1, num2))
                except ValueError as e:
                    print("Error:", e)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    calculator()
 