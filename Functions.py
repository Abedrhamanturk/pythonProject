def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Addition result:", add(num1, num2))
print("Subtraction result:", subtract(num1, num2))
print("Multiplication result:", multiply(num1, num2))
print("Division result:", divide(num1, num2))