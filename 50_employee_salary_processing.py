employees = [("Asha", "IT", 48000), ("Ravi", "Sales", 62000), ("Neha", "IT", 75000)]
high_earners = list(filter(lambda e: e[2] > 50000, employees))
raised_salaries = list(map(lambda e: (e[0], e[1], e[2] * 1.10), employees))
sorted_employees = sorted(employees, key=lambda e: e[2])
print("Earning more than 50000 =", high_earners)
print("Salary after 10% increase =", raised_salaries)
print("Sorted by salary =", sorted_employees)
