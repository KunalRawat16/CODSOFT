import json
import os

class Contact:
    def __init__(self, name, phone, email, address):
        """
        Initialize a contact with name, phone number, email, and address.
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        """
        Convert the contact object to a dictionary.
        """
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address
        }

class ContactManager:
    def __init__(self, filename='contacts.json'):
        """
        Initialize the ContactManager with a filename for storing contacts.
        """
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """
        Load contacts from a JSON file.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [Contact(**contact) for contact in json.load(file)]
        return []

    def save_contacts(self):
        """
        Save contacts to a JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def add_contact(self, contact):
        """
        Add a new contact.
        """
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact {contact.name} added successfully.")

    def view_contacts(self):
        """
        Display a list of all saved contacts.
        """
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, query):
        """
        Search contacts by name or phone number.
        """
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if results:
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No contacts found.")

    def update_contact(self, name):
        """
        Update contact details by name.
        """
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                self.save_contacts()
                print(f"Contact {contact.name} updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        """
        Delete a contact by name.
        """
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"Contact {contact.name} deleted successfully.")
                return
        print("Contact not found.")

def display_menu():
    """
    Display the menu options for the Contact Management System.
    """
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    """
    Main function to run the Contact Management System.
    """
    contact_manager = ContactManager()

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_manager.add_contact(contact)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_manager.search_contact(query)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            contact_manager.update_contact(name)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '6':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
