
server_ip = ("192.168.1.100",)

allowed_ips = ["192.168.1.2", "192.168.1.3"]

def add_ip():
    ip = input("Enter new IP: ")
    allowed_ips.append(ip)
    print("IP Added.")

def remove_ip():
    ip = input("Enter IP to remove: ")

    if ip in allowed_ips:
        allowed_ips.remove(ip)
        print("IP Removed.")
    else:
        print("IP not found.")

while True:

    print("\n1.Show Configuration")
    print("2.Add Allowed IP")
    print("3.Remove Allowed IP")
    print("4.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        print("Server IP:", server_ip[0])
        print("Allowed IPs:", allowed_ips)

    elif ch == "2":
        add_ip()

    elif ch == "3":
        remove_ip()

    elif ch == "4":
        break

    else:
        print("Invalid choice")
