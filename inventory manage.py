# Inventory Management

inventory = {}

def add_product():
    name = input("Enter product name: ")
    qty = int(input("Enter quantity: "))
    inventory[name] = qty
    print("Product added.")

def update_product():
    name = input("Enter product name: ")

    if name in inventory:
        qty = int(input("Enter new quantity: "))
        inventory[name] = qty
        print("Quantity updated.")
    else:
        print("Product not found.")

def remove_product():
    name = input("Enter product name: ")

    if name in inventory:
        if inventory[name] == 0:
            del inventory[name]
            print("Product removed.")
        else:
            print("Quantity is not zero.")
    else:
        print("Product not found.")

def highest_stock():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        product = max(inventory, key=inventory.get)
        print("Highest Stock Product:", product)
        print("Quantity:", inventory[product])

while True:

    print("\n1.Add Product")
    print("2.Update Product")
    print("3.Remove Product")
    print("4.Highest Stock")
    print("5.Total Products")
    print("6.Display Inventory")
    print("7.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        update_product()

    elif choice == "3":
        remove_product()

    elif choice == "4":
        highest_stock()

    elif choice == "5":
        print("Total Products:", len(inventory))

    elif choice == "6":
        print(inventory)

    elif choice == "7":
        break

    else:
        print("Invalid choice")
