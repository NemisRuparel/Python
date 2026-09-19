# Match Statement

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Add")
    case 2:
        print("Subtract")
    case 3:
        print("Multiply")
    case 4:
        print("Divide")
    case _:
        print("Invalid choice")