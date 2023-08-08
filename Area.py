def triangle_area(base, height):
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    return area

def circle_area(radius):
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius * radius
    return area
def rectangle_area(length, width):
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    return area
def check_area(area):
    if area >= 10:
        print("Area is big")
    elif area < 10 and area > 0:
        print("Area is small")
    elif area <= 0:
        print("Invalid inputs")
triangle_area_result = triangle_area(base=0, height=0)
print("Area of the triangle is:", triangle_area_result)
check_area(triangle_area_result)
circle_area_result = circle_area(radius=0)
print("Area of the circle is:", circle_area_result)
check_area(circle_area_result)
rectangle_area_result = rectangle_area(length=0,width=0)
print("Area of the rectangle is:", rectangle_area_result)
check_area(rectangle_area_result)