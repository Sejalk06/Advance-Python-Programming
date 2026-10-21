books = {}

def add_book(title):
    books[title] = True

def issue_book(title):
    if title in books and books[title]:
        books[title] = False
        print("Book issued")
    else:
        print("Book unavailable")

def return_book(title):
    if title in books:
        books[title] = True
        print("Book returned")
    else:
        print("Book not found")

def search_book(title):
    print("Available" if books.get(title, False) else "Not available or not found")

def display_books():
    for title, available in books.items():
        if available:
            print(title)

while True:
    print("1.Add 2.Issue 3.Return 4.Search 5.Display available 6.Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_book(input("Book title: "))
    elif choice == "2":
        issue_book(input("Book title: "))
    elif choice == "3":
        return_book(input("Book title: "))
    elif choice == "4":
        search_book(input("Book title: "))
    elif choice == "5":
        display_books()
    elif choice == "6":
        break
