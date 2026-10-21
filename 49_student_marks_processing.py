students = [("Asha", 82), ("Ravi", 69), ("Neha", 91), ("Amit", 77)]
average = sum(map(lambda s: s[1], students)) / len(students)
above_75 = list(filter(lambda s: s[1] > 75, students))
sorted_students = sorted(students, key=lambda s: s[1])
print("Average marks =", average)
print("Above 75 =", above_75)
print("Sorted by marks =", sorted_students)
