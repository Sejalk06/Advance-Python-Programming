def grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    return "Fail"

students = []
n = int(input("Number of students: "))
for i in range(n):
    name = input("Student name: ")
    roll = input("Roll number: ")
    marks = [float(input("Marks in subject " + str(j + 1) + ": ")) for j in range(5)]
    total = sum(marks)
    percentage = total / 5
    students.append({"name": name, "roll": roll, "marks": marks, "total": total,
                     "percentage": percentage, "grade": grade(percentage)})

for s in students:
    print(s["name"], s["roll"], "Total:", s["total"], "Percentage:", s["percentage"], "Grade:", s["grade"])
print("Class average percentage =", sum(s["percentage"] for s in students) / len(students))
print("Highest scorer =", max(students, key=lambda s: s["total"])["name"])
print("Lowest scorer =", min(students, key=lambda s: s["total"])["name"])
