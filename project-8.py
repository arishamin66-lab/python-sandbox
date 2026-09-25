contacts = {}

inp = 0

while inp != 6:
    print("\n--- Contact Book ---")
    inp = int(input("""1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. Display all contacts
6. Exit
Select an option: """))

    if inp == 1:
        name = input("Enter name: ").strip()
        contact_number = input("Enter number: ").strip()
        contacts[name] = contact_number
        print(f"Contact '{name}' added successfully.")

    elif inp == 2:
        name = input("Enter name to search: ").strip()
        if name in contacts:
            print(f"Found: {name} -> {contacts[name]}")
        else:
            print(f"No contact found for '{name}'.")

    elif inp == 3:
        name = input("Enter current name to update: ").strip()
        if name in contacts:
            new_name = input("Enter new name (leave blank to keep current): ").strip()
            new_number = input("Enter new number (leave blank to keep current): ").strip()

            # Handle phone number update
            updated_number = new_number if new_number else contacts[name]

            # Handle name update
            if new_name and new_name != name:
                del contacts[name]
                contacts[new_name] = updated_number
            else:
                contacts[name] = updated_number

            print("Contact updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    elif inp == 4:
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"Deleted contact '{name}'.")
        else:
            print(f"Contact '{name}' not found.")

    elif inp == 5:
        if contacts:
            print("\nAll Contacts:")
            for name, number in contacts.items():
                print(f"- {name}: {number}")
        else:
            print("Contact book is empty.")

    elif inp == 6:
        print("Exiting Contact Book. Goodbye!")