def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

if __name__ == "__main__":
    print("Running internal tests...")
    print("5 + 3 =", perform_operation(5, 3, 'add'))
    print("10 / 0 =", perform_operation(10, 0, 'divide'))
    print("7 * 2 =", perform_operation(7, 2, 'multiply'))
    print("Invalid op =", perform_operation(4, 2, 'mod'))
