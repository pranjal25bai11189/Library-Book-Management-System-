# Library Book Management System

library = {
    "Harry Potter and the Philosopher's Stone": "Available",
    "Atomic Habits": "Available",
    "The Alchemist": "Available",
    "Think Like a Monk": "Available",
    "Rich Dad Poor Dad": "Available",
    "The Power of Subconscious Mind": "Available",
    "Wings of Fire": "Available",
    "The Monk Who Sold His Ferrari": "Available",
    "Ikigai": "Available",
    "The Subtle Art of Not Giving a F*ck": "Available",
    "Deep Work": "Available",
    "Can't Hurt Me": "Available",
    "A Brief History of Time": "Available",
    "The Psychology of Money": "Available",
    "Zero to One": "Available"
}

def add_book():
    book = input("Enter book title: ").strip()
    if book in library:
        print("This book already exists in the library.\n")
    else:
        library[book] = "Available"
        print(f"'{book}' added successfully!\n")

def borrow_book():
    book = input("Enter book title to borrow: ").strip()
    if book not in library:
        print("Book not found in library.\n")
    else:
        if library[book] == "Available":
            library[book] = "Issued"
            print(f"You have borrowed '{book}'.\n")
        else:
            print("Sorry, this book is already issued.\n")

def return_book():
    book = input("Enter book title to return: ").strip()
    if book not in library:
        print("This book does not belong to this library.\n")
    else:
        if library[book] == "Issued":
            library[book] = "Available"
            print(f"'{book}' returned successfully!\n")
        else:
            print("This book was not issued.\n")

def show_books():
    print("\n===== Library Books =====")
    for book, status in library.items():
        print(f"{book} - {status}")
    print("=========================\n")

def search_book():
    book = input("Enter book title to search: ").strip()
    if book in library:
        print(f"{book} is currently {library[book]}.\n")
    else:
        print("Book not found.\n")

def main():
    while True:
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Show All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            show_books()
        elif choice == "5":
            search_book()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.\n")

main()