balance = 0
history = []

def deposit(amount):
    global balance
    balance += amount
    history.append("Deposited: " + str(amount))

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        history.append("Withdrawn: " + str(amount))

while True:
    print("1.Deposit 2.Withdraw 3.Balance 4.History 5.Exit")
    choice = input("Choose: ")
    if choice == "1":
        amount = float(input("Amount: "))
        deposit(amount)
    elif choice == "2":
        amount = float(input("Amount: "))
        withdraw(amount)
    elif choice == "3":
        print("Balance =", balance)
    elif choice == "4":
        print(history)
    elif choice == "5":
        break
    else:
        print("Invalid choice")
