#simple two number calculator code in python

print("Simple Calculator")

# 1. Get the numbers and the operation from the user
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# 2. Check the operation and calculate the result
if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operation == "/":
    # A quick safety check to prevent a crash (division by zero)
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

else:
    print("Invalid operation selected.")
    