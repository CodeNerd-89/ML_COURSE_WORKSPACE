# Make a function that calculates and prints the surface area and volume of a sphere
import math

def sphere_surface_area_volume(radius):
    surface_area = 4 * math.pi * radius ** 2
    volume = (4/3) * math.pi * radius ** 3
    return surface_area, volume

radius = float(input("Enter the radius of the sphere: "))

surface_area, volume = sphere_surface_area_volume(radius)

print(f"Surface Area of Sphere = {surface_area:.2f}")
print(f"Volume of Sphere = {volume:.2f}")
