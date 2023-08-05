def triangle_area(base, height):
    area = 0.5 * base * height
    return area

def circle_area(radius):
    area = 3.14 * radius * radius
    return area

def rectangle_area(length, width):
    area = length * width
    return area

def check_area(area):
    if area >= 10:
        print("Area is bigger than 10")
    elif area < 10 and area > 0:
        print("Area is smaller than 10")
    elif area <= 0:
        print("Invalid inputs")

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle_area_result = triangle_area(base, height)
print("Area of the triangle is:", triangle_area_result)
check_area(triangle_area_result)

radius = float(input("Enter the radius of the circle: "))
circle_area_result = circle_area(radius)
print("Area of the circle is:", circle_area_result)
check_area(circle_area_result)
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_area_result = rectangle_area(length, width)
print("Area of the rectangle is:", rectangle_area_result)
check_area(rectangle_area_result)