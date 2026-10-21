def electricity_bill(units):
    if units <= 100:
        return units * 3
    elif units <= 200:
        return 100 * 3 + (units - 100) * 5
    else:
        return 100 * 3 + 100 * 5 + (units - 200) * 7

units = float(input("Enter units consumed: "))
print("Electricity bill =", electricity_bill(units))
