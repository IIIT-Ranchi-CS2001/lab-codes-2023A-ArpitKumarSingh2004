import math

x1 = float(input("Enter x-coordinate for Point 1: "))
y1 = float(input("Enter y-coordinate for Point 1: "))
z1 = float(input("Enter z-coordinate for Point 1: "))
point1 = (x1, y1, z1)

x2 = float(input("Enter x-coordinate for Point 2: "))
y2 = float(input("Enter y-coordinate for Point 2: "))
z2 = float(input("Enter z-coordinate for Point 2: "))
point2 = (x2, y2, z2)

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

print("Point 1:", point1)
print("Point 2:", point2)
print("Euclidean Distance:", distance)
