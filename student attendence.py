attendance = {}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days:

    names = input("Enter students for " + day + " (space separated): ")
    attendance[day] = set(names.split())

print("\nAttendance Record")
print(attendance)

all_students = set()

for students in attendance.values():
    all_students = all_students.union(students)

print("\nStudents attended during the week:")
print(all_students)

only_once = set()

for student in all_students:
    count = 0

    for students in attendance.values():
        if student in students:
            count += 1

    if count == 1:
        only_once.add(student)

print("\nStudents attended only one class:")
print(only_once)

print("\nTotal Unique Students:")
print(len(all_students))
