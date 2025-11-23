# ============================================================
#              LIBRARY BOOK MANAGEMENT SYSTEM
#                    Python Project (200 Lines)
# ============================================================

# This project uses:
# - Functions
# - Loops
# - Dictionaries
# - Conditional Statements
#
# It manages:
# * Adding Books
# * Borrowing Books
# * Returning Books
# * Searching Books
# * Showing All Books
#
# ============================================================


# ------------------------------------------------------------
#                 GLOBAL LIBRARY DICTIONARY
# ------------------------------------------------------------

library = {
    "Harry Potter": "Available",
    "Atomic Habits": "Available",
    "The Alchemist": "Available",
    "Ikigai": "Available",
    "The Power of Habit": "Available",
    "Zero to One": "Available",
    "Deep Work": "Available",
    "Think and Grow Rich": "Available",
    "The Psychology of Money": "Available",
    "Rich Dad Poor Dad": "Available",
    "Clean Code": "Available",
    "Python Basics": "Available",
    "Sapiens": "Available",
    "The Subtle Art of Not Giving a F*ck": "Available",
    "Wings of Fire": "Available"
}

# ------------------------------------------------------------
#               Helper Function: Line Break
# ------------------------------------------------------------

def line():
    """Prints a decorative line for better UI."""
    print("\n" + "-" * 55 + "\n")


# ------------------------------------------------------------
#                  Function: Add New Book
# ------------------------------------------------------------

def add_book():
    """
    Adds a new book to the library.
    Checks if the book already exists.
    """
    line()
    print("📘 ADD NEW BOOK")
    line()

    book = input("Enter book title: ").strip()

    if book in library:
        print(f"❗ '{book}' already exists in the library.")
    else:
        library[book] = "Available"
        print(f"✅ '{book}' has been added successfully!")

    line()


# ------------------------------------------------------------
#              Function: Borrow (Issue) Book
# ------------------------------------------------------------

def borrow_book():
    """
    Allows user to borrow a book if it's available.
    """
    line()
    print("📕 BORROW BOOK")
    line()

    book = input("Enter book title to borrow: ").strip()

    if book not in library:
        print(f"❗ '{book}' does not exist in the library.")
    else:
        if library[book] == "Available":
            library[book] = "Issued"
            print(f"✅ You have borrowed '{book}'.")
        else:
            print(f"⚠ '{book}' is already issued.")

    line()


# ------------------------------------------------------------
#             Function: Return Previously Issued Book
# ------------------------------------------------------------

def return_book():
    """
    Allows user to return a previously issued book.
    """
    line()
    print("📙 RETURN BOOK")
    line()

    book = input("Enter book title to return: ").strip()

    if book not in library:
        print(f"❗ '{book}' does not exist in the library.")
    else:
        if library[book] == "Issued":
            library[book] = "Available"
            print(f"✅ '{book}' has been returned successfully!")
        else:
            print(f"⚠ '{book}' was not issued.")

    line()


# ------------------------------------------------------------
#             Function: Search for a Book
# ------------------------------------------------------------

def search_book():
    """
    Searches for a book and shows its status.
    """
    line()
    print("🔍 SEARCH BOOK")
    line()

    book = input("Enter book title to search: ").strip()

    if book in library:
        print(f"📗 '{book}' is currently: {library[book]}")
    else:
        print(f"❗ '{book}' not found in library.")

    line()


# ------------------------------------------------------------
#           Function: Display All Books with Status
# ------------------------------------------------------------

def show_books():
    """
    Displays all books in the library with their status.
    """
    line()
    print("📚 ALL BOOKS IN LIBRARY")
    line()

    count = 1
    for book, status in library.items():
        print(f"{count}. {book}  -->  {status}")
        count += 1

    line()


# ------------------------------------------------------------
#               Menu Display Function (UI)
# ------------------------------------------------------------

def show_menu():
    """
    Prints the main menu.
    """
    print("======================================================")
    print("         📘 LIBRARY BOOK MANAGEMENT SYSTEM")
    print("======================================================")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Show All Books")
    print("5. Search Book")
    print("6. Exit")
    print("======================================================")


# ------------------------------------------------------------
#                   MAIN FUNCTION (Driver)
# ------------------------------------------------------------

def main():
    """
    Controls the entire flow of the program.
    Uses a loop so user can perform multiple actions.
    """
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("\n❗ Invalid input! Please enter a number.")
            continue

        if choice == 1:
            add_book()

        elif choice == 2:
            borrow_book()

        elif choice == 3:
            return_book()

        elif choice == 4:
            show_books()

        elif choice == 5:
            search_book()

        elif choice == 6:
            print("\n📄 Exiting the system... Goodbye!")
            break

        else:
            print("❗ Please select a valid option (1-6).")


# ------------------------------------------------------------
#                    Program Execution
# ------------------------------------------------------------

if _name_ == "_main_":
    main()

# ============================================================
# END OF PROJECT (Approximately 200 Lines)
# ============================================================
