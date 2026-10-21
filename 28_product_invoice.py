products = {}

def add_product(name, price, quantity):
    products[name] = [price, quantity]

def remove_product(name):
    products.pop(name, None)

def invoice(coupon=0):
    subtotal = sum(price * quantity for price, quantity in products.values())
    discounted = subtotal - subtotal * coupon / 100
    gst = discounted * 0.18
    return subtotal, discounted, gst, discounted + gst

while True:
    print("1.Add product 2.Remove product 3.Invoice 4.Exit")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Product name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        add_product(name, price, quantity)
    elif choice == "2":
        remove_product(input("Product name: "))
    elif choice == "3":
        coupon = float(input("Coupon discount percentage: "))
        subtotal, discounted, gst, total = invoice(coupon)
        print("Subtotal:", subtotal, "After discount:", discounted, "GST:", gst, "Final:", total)
    elif choice == "4":
        break
