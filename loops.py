def sum_numbers(a, b):
    return a + b
def subtract_numbers(a, b):
    return a - b
def multiply_numbers(a, b):
    return a * b
def divide_numbers(a, b):
    return a / b
def calculate_triangle_area(base, height):
    return 0.5 * base * height
def calculate_circle_area(radius):
    return 3.14* radius ** 2
def calculate_rectangle_area(length, width):
    return length * width
while True:
    choice = int(input(      "Main Menu:\n"
                       "1. Sum\n"
                       "2. Subtract\n"
                       "3. Multiply\n"
                       "4. Division\n"
                       "5. Calculate triangle area\n"
                       "6. Calculate circle area\n"
                       "7. Calculate rectangle area\n"
                              "8. Exit\n"
                       "Enter your choice: "))
    if choice == 8:
        print("Exiting...")
        break
    if choice < 1 or choice > 8:
        print("Invalid choice. Please select a valid option.")
        continue
    if choice <5 and choice >0:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    elif choice == 5:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
    elif choice == 6:
        radius = float(input("Enter the radius of the circle: "))
    elif choice == 7:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
    if choice == 1:
        result = sum_numbers(a, b)
    elif choice == 2:
        result = subtract_numbers(a, b)
    elif choice == 3:
        result = multiply_numbers(a, b)
    elif choice == 4:
        result = divide_numbers(a, b)
    elif choice == 5:
        result = calculate_triangle_area(base, height)
    elif choice == 6:
        result = calculate_circle_area(radius)
    elif choice == 7:
        result = calculate_rectangle_area(length, width)
    print("Result:", result)
