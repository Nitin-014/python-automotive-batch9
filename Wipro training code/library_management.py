# Library Book Management System
# This program demonstrates basic Python scripting concepts

# Dictionary to store books
books = {"horur",}

while True:
    print("\nLibrary Book Management")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Show All Books")
    print("5. Exit")

    # Taking user choice and type casting to int
    choice = int(input("Enter your choice: "))

    # Add new book
    if choice == 1:
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        books[book_id] = book_name
        print("Book added successfully")

    # Remove book
    elif choice == 2:
        book_id = input("Enter Book ID to remove: ")
        if book_id in books:
            del books[book_id]
            print("Book removed successfully")
        else:
            print("Book not found")

    # Search for a book
    elif choice == 3:
        book_id = input("Enter Book ID to search: ")
        if book_id in books:
            print("Book Found:", books[book_id])
        else:
            print("Book not found")

    # Show all books
    elif choice == 4:
        if books:
            print("Books available in library:")
            for book_id in books:
                print(book_id, ":", books[book_id])
        else:
            print("No books available")

    # Exit program
    elif choice == 5:
        print("Exiting Library Management System")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")
