# contact_manager.py

FILE_NAME = "contacts.txt"


def add_contact(name, phone):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone}\n")
    print("Contact added successfully.")


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.")
            else:
                for contact in contacts:
                    name, phone = contact.strip().split(",")
                    print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("Contact file not found.")


while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        add_contact(name, phone)

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
