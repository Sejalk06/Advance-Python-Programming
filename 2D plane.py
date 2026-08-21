import math

points = []

n = int(input("Enter number of points: "))

for i in range(n):
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    points.append((x, y))

def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

print("\nPoints List")
print(points)

a = int(input("Enter first point index: "))
b = int(input("Enter second point index: "))

print("Distance =", distance(points[a], points[b]))

def farthest_point(points):
    far = points[0]
    max_dist = math.sqrt(far[0]**2 + far[1]**2)

    for p in points:
        d = math.sqrt(p[0]**2 + p[1]**2)
        if d > max_dist:
            max_dist = d
            far = p

    return far

print("Farthest Point =", farthest_point(points))
