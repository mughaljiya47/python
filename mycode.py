import json
import os
CONTACT_FILE = "contact.json"  # Fixed typo here
def load_contact():
    if os.path.exists(CONTACT_FILE):  # Fixed typo: changed "exist" to "exists"
        with open(CONTACT_FILE, "r") as file:
            return json.load(file)
    return {}
def save_contact(contact):
    with open(CONTACT_FILE, "w") as file:  # Fixed the issue with `with` syntax
        json.dump(contact, file, indent=4)
def add_contact(name, email, phone_no):
    contact = load_contact()
    contact[name] = {"Phone": phone_no, "Email": email}  # Fixed the dictionary keys
    save_contact(contact)
    print("Phone No Saved")
def search_contact(name):
    contact = load_contact()
    if name in contact:
        return contact[name]
    else:
        return "Not Found"
def update_contact(name, phone_no=None, email=None):
    contact = load_contact()
    if name in contact:
        if phone_no:
            contact[name]["Phone"] = phone_no  # Fixed the dictionary key to match the original one
        if email:
            contact[name]["Email"] = email  # Fixed the dictionary key to match the original one
        save_contact(contact)
        print("Contact has been updated")
    else:
        return "Not Found"
def del_contact(name):
    contact = load_contact()
    if name in contact:
        del contact[name]
        save_contact(contact)
        print("Contact has been Deleted")
    else:
        return "Not Found"
if __name__ == "__main__":
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Show Contact List")
        print("6. Exit")
        choice = int(input("Enter Your Option: "))
        if choice == 1:
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone_no = input("Enter Phone No: ")
            add_contact(name, email, phone_no)
        elif choice == 2:
            name = input("Search Your Contact by Name: ")
            print(search_contact(name))
        elif choice == 3:
            name = input("Enter Name to Update: ")
            phone = input("New Phone No (Press Enter to Skip): ")
            email = input("Enter New Email (Press Enter for Skip): ")
            update_contact(name, phone if phone else None, email if email else None)
        elif choice == 4:
            name = input("Enter Name to Delete: ")
            del_contact(name)
        elif choice == 5:
            contact = load_contact()
            for name, details in contact.items():  # Fixed `contact.item()` to `contact.items()`
                print(f"{name} - {details}")
        elif choice == 6:
            print("Exiting from Contact Book")
            break
        else:
            print("Invalid Choice")