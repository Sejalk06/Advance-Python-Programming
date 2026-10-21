def total_bill(prices, quantities, discount):
    total = sum(p * q for p, q in zip(prices, quantities))
    return total - total * discount / 100

prices = list(map(float, input("Enter item prices: ").split()))
quantities = list(map(int, input("Enter quantities in same order: ").split()))
discount = float(input("Enter discount percentage: "))
print("Final bill =", total_bill(prices, quantities, discount))
