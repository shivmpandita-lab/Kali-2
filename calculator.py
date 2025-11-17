def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def main():
    print("Simple Addition and Subtraction Calculator")
    choice = input("Type + for addition, - for subtraction: ").strip()
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == '+':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '-':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    else:
        print("Invalid operation. Please choose + or -.")

if __name__ == "__main__":
    main()