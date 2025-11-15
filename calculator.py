def calculator():
    print("\n=== Simple Python Console Calculator ===")
    print("Available operators: +  -  *  /  %  **")
    print("----------------------------------------")

    # Taking inputs
    try:
        x = float(input("Enter first number (X): "))
        y = float(input("Enter second number (Y): "))
    except ValueError:
        print("❌ Invalid number input. Please enter numeric values.")
        return
    
    operator = input("Choose an operator: ")

    # Perform operation based on selected operator
    print("----------------------------------------")

    if operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "*":
        result = x * y
    elif operator == "/":
        if y == 0:
            print("❌ Error: Division by zero is not allowed!")
            return
        result = x / y
    elif operator == "%":
        if y == 0:
            print("❌ Error: Modulus by zero is not allowed!")
            return
        result = x % y
    elif operator == "**":
        result = x ** y
    else:
        print("❌ Invalid operator selected.")
        return

    # Print result
    print(f"✔ Result: {x} {operator} {y} = {result}")
    print("========================================")


# Run the calculator
calculator()
