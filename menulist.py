def display():
    print("Menu List")
    print("1. Add a name")
    print("2. Change a name")
    print("3. Delete a name")
    print("4. View all names")
    print("5. Exit")
names = []

while True:
    display()
    choice = int(input("Enter your choice (1-5):"))

    if choice == 1:
        name = input("Enter the name to add:")
        names.append(name)
        print(f"Added {name} to the list. ")

    elif choice == 2:
        print("Current names:", names)
        old_name = input("Enter the name to change: ")
        new_name = input("Enter the new name: ") 
        names[names.index(old_name)] = new_name
        print(f"Changed {old_name} to {new_name}")

    elif choice == 3:
        print("Current names:", names)
        name_delete = input("Enter the name you want to delete:")
        names.remove(name_delete)

    elif choice ==4:
        print("Current names:" )
        for name in names:
            print(name)

    elif choice ==5:
        print("Goodbye")
        break




