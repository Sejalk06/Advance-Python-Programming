simple_interest = lambda p, r, t: p * r * t / 100
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
print("Simple interest =", simple_interest(p, r, t))
