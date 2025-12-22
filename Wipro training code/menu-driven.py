while True:
    print("\nMENU")
    print("1. Square the number")
    print("2. Cube the number")
    print("3. Exit")

    choice = int(input("Enter your choice (1-3): "))    # Taking user choice

    if choice == 1:                               
        num = float(input("Enter a number: "))            # If user selects square option
        print("Square of", num, "is", num ** 2)

    elif choice == 2:
        num = float(input("Enter a number: "))            # If user selects cube option
        print("Cube of", num, "is", num ** 3)

    elif choice == 3:
        print("Exiting program...")                     # If user selects exit option
        break

    else:                                               # If user enters invalid choice
        print("Invalid choice! Please select 1, 2, or 3.")
