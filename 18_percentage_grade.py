def percentage_grade(marks):
    percentage = sum(marks) / len(marks)
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"
    return percentage, grade

marks = []
for i in range(5):
    marks.append(float(input("Enter marks for subject " + str(i + 1) + ": ")))
percentage, grade = percentage_grade(marks)
print("Percentage =", percentage)
print("Grade =", grade)
