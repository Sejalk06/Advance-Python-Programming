project1 = {"Rahul", "Anjali", "Priya", "Rohit"}

project2 = {"Priya", "Rohit", "Amit", "Neha"}

print("Employees in Project 1")
print(project1)

print("\nEmployees in Project 2")
print(project2)

print("\nWorking on Both Projects")
print(project1.intersection(project2))

print("\nWorking Only on Project 1")
print(project1.difference(project2))

print("\nWorking Only on Project 2")
print(project2.difference(project1))

print("\nTotal Unique Employees")
print(project1.union(project2))
