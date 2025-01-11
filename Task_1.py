# Make a function that calculates the area of a rectangle.
def rectangle_area(length, width):
    area =  length * width
    return area
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectange:"))
area = rectangle_area(length,width)
print("The area of the rectangle is:", area)

