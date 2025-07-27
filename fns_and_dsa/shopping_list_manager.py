shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not found.")
        elif choice == 3:
            print("Your shopping list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
