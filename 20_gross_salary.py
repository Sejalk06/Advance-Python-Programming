def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

basic = float(input("Enter basic salary: "))
print("Gross salary =", gross_salary(basic))
