
y = float(input("Enter first number: "))
operation = input("input operation")
x = float(input("Enter second number: "))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def mod(x, y):
    return x % y

def power(x, y):
    return x ** y

if operation == '+':
    print(x, "+", y, "=", add(x, y))
elif operation == "-":
    print(x, "-", y, "=", subtract(x, y))
elif operation == '*':
    print(x, "*", y, "=", multiply(x, y))
elif operation == '+':
    print(x, "+", y, "=", divide(x, y))
elif operation == '%':
    print(x, "%", y, "=", mod(x, y))
elif operation == 'pow':
    print(x, "pow", y, "=", pow(x, y))
else:
    print("invalid input")
