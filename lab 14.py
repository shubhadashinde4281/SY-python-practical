Phonebook = {}

while True:
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        Phonebook[name] = number
        print("Contact added successfully!")

    elif choice == 2:
        name = input("Enter name to update: ")
        if name in Phonebook:
            number = input("Enter new phone number: ")
            Phonebook[name] = number
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == 3:
        name = input("Enter name to delete: ")
        if name in Phonebook:
            del Phonebook[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == 4:
        print("\nPhonebook Contacts:")
        for name, number in Phonebook.items():
            print(name, ":", number)

    elif choice == 5:
        print("Exiting Phonebook...")
        break

    else:
        print("Invalid choice! Please try again.")