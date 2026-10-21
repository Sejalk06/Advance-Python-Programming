def electricity_bill(units):
    if units <= 100:
        amount = units * 3
    elif units <= 200:
        amount = 100 * 3 + (units - 100) * 5
    else:
        amount = 100 * 3 + 100 * 5 + (units - 200) * 7
    fixed_charge = 50
    tax = amount * 0.05
    discount = amount * 0.02 if units < 100 else 0
    return amount + fixed_charge + tax - discount

units = float(input("Enter units consumed: "))
print("Final electricity bill =", electricity_bill(units))
