"""
Simple Contact Management System
A beginner-friendly console application for managing contacts with
persistent file storage.

Author: Professional Software Developer
Date: January 30, 2026
"""

import json
import os
import re


# Global constant for the contacts file
CONTACTS_FILE = "contacts.json"


def load_contacts():
    """
    Load contacts from the JSON file.
    If the file doesn't exist, return an empty dictionary.
    
    Returns:
        dict: Dictionary containing all contacts with ID as key
    """
    # Check if the contacts file exists
    if os.path.exists(CONTACTS_FILE):
        try:
            # Open and read the file
            with open(CONTACTS_FILE, 'r') as file:
                contacts = json.load(file)
                return contacts
        except json.JSONDecodeError:
            # Handle corrupted file
            print("⚠️  Warning: Contacts file is corrupted. Starting with empty contacts.")
            return {}
        except Exception as e:
            # Handle other file reading errors
            print(f"⚠️  Error loading contacts: {e}")
            return {}
    else:
        # Return empty dictionary if file doesn't exist
        return {}


def save_contacts(contacts):
    """
    Save contacts to the JSON file for persistent storage.
    
    Args:
        contacts (dict): Dictionary containing all contacts
    
    Returns:
        bool: True if save was successful, False otherwise
    """
    try:
        # Write contacts to file with proper formatting
        with open(CONTACTS_FILE, 'w') as file:
            json.dump(contacts, file, indent=4)
        return True
    except Exception as e:
        # Handle file writing errors
        print(f"❌ Error saving contacts: {e}")
        return False


def validate_phone(phone):
    """
    Validate phone number format.
    Accepts various formats: (123) 456-7890, 123-456-7890, 1234567890, etc.
    
    Args:
        phone (str): Phone number to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    
    # Check if it has 10 digits (standard phone number length)
    if len(digits_only) >= 10:
        return True
    
    return False


def validate_email(email):
    """
    Validate email address format using regex pattern.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    # Basic email validation pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    
    return False


def generate_contact_id(contacts):
    """
    Generate a unique ID for a new contact.
    
    Args:
        contacts (dict): Existing contacts dictionary
    
    Returns:
        str: Unique contact ID
    """
    # If no contacts exist, start with ID 1
    if not contacts:
        return "1"
    
    # Find the maximum ID and increment it
    max_id = max([int(id) for id in contacts.keys()])
    return str(max_id + 1)


def display_header(title):
    """
    Display a formatted header for different sections.
    
    Args:
        title (str): Title to display
    """
    print("\n" + "="*60)
    print(f"{title.center(60)}")
    print("="*60)


def display_menu():
    """
    Display the main menu options to the user.
    """
    display_header("CONTACT MANAGEMENT SYSTEM")
    print("\n📋 MENU OPTIONS:")
    print("  1. Add New Contact")
    print("  2. View All Contacts")
    print("  3. Search Contact")
    print("  4. Edit Contact")
    print("  5. Delete Contact")
    print("  6. Exit")
    print("\n" + "-"*60)


def add_contact(contacts):
    """
    Add a new contact to the contact list.
    
    Args:
        contacts (dict): Current contacts dictionary
    
    Returns:
        dict: Updated contacts dictionary
    """
    display_header("ADD NEW CONTACT")
    
    # Get contact name
    while True:
        name = input("\nEnter contact name: ").strip()
        if name:
            break
        print("❌ Name cannot be empty. Please try again.")
    
    # Get and validate phone number
    while True:
        phone = input("Enter phone number: ").strip()
        if validate_phone(phone):
            break
        print("❌ Invalid phone number. Please enter at least 10 digits.")
    
    # Get and validate email address
    while True:
        email = input("Enter email address: ").strip()
        if validate_email(email):
            break
        print("❌ Invalid email format. Please enter a valid email (e.g., user@example.com).")
    
    # Generate unique ID for the contact
    contact_id = generate_contact_id(contacts)
    
    # Create contact dictionary
    contacts[contact_id] = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    # Save to file
    if save_contacts(contacts):
        print(f"\n✅ Contact '{name}' added successfully! (ID: {contact_id})")
    else:
        print("\n❌ Failed to save contact.")
    
    return contacts


def view_all_contacts(contacts):
    """
    Display all contacts in a formatted table.
    
    Args:
        contacts (dict): Dictionary containing all contacts
    """
    display_header("ALL CONTACTS")
    
    # Check if there are any contacts
    if not contacts:
        print("\n📭 No contacts found. The contact list is empty.")
        return
    
    # Display table header
    print(f"\n{'ID':<5} {'Name':<20} {'Phone':<18} {'Email':<25}")
    print("-"*70)
    
    # Display each contact
    for contact_id, contact_info in contacts.items():
        print(f"{contact_id:<5} {contact_info['name']:<20} {contact_info['phone']:<18} {contact_info['email']:<25}")
    
    print(f"\n📊 Total contacts: {len(contacts)}")


def search_contact(contacts):
    """
    Search for a contact by name, phone, or email.
    
    Args:
        contacts (dict): Dictionary containing all contacts
    """
    display_header("SEARCH CONTACT")
    
    if not contacts:
        print("\n📭 No contacts available to search.")
        return
    
    # Get search query
    query = input("\nEnter name, phone, or email to search: ").strip().lower()
    
    if not query:
        print("❌ Search query cannot be empty.")
        return
    
    # Search for matching contacts
    found_contacts = {}
    for contact_id, contact_info in contacts.items():
        if (query in contact_info['name'].lower() or 
            query in contact_info['phone'] or 
            query in contact_info['email'].lower()):
            found_contacts[contact_id] = contact_info
    
    # Display results
    if found_contacts:
        print(f"\n🔍 Found {len(found_contacts)} matching contact(s):")
        print(f"\n{'ID':<5} {'Name':<20} {'Phone':<18} {'Email':<25}")
        print("-"*70)
        
        for contact_id, contact_info in found_contacts.items():
            print(f"{contact_id:<5} {contact_info['name']:<20} {contact_info['phone']:<18} {contact_info['email']:<25}")
    else:
        print(f"\n❌ No contacts found matching '{query}'.")


def edit_contact(contacts):
    """
    Edit an existing contact's information.
    
    Args:
        contacts (dict): Dictionary containing all contacts
    
    Returns:
        dict: Updated contacts dictionary
    """
    display_header("EDIT CONTACT")
    
    if not contacts:
        print("\n📭 No contacts available to edit.")
        return contacts
    
    # Display all contacts first
    print(f"\n{'ID':<5} {'Name':<20} {'Phone':<18}")
    print("-"*45)
    for contact_id, contact_info in contacts.items():
        print(f"{contact_id:<5} {contact_info['name']:<20} {contact_info['phone']:<18}")
    
    # Get contact ID to edit
    contact_id = input("\nEnter the ID of the contact to edit: ").strip()
    
    # Check if contact exists
    if contact_id not in contacts:
        print(f"❌ Contact with ID '{contact_id}' not found.")
        return contacts
    
    # Display current contact information
    print(f"\nCurrent information for '{contacts[contact_id]['name']}':")
    print(f"  Name: {contacts[contact_id]['name']}")
    print(f"  Phone: {contacts[contact_id]['phone']}")
    print(f"  Email: {contacts[contact_id]['email']}")
    
    print("\n💡 Press Enter to keep current value, or enter new value to update.")
    
    # Get new name (or keep current)
    new_name = input(f"\nNew name [{contacts[contact_id]['name']}]: ").strip()
    if new_name:
        contacts[contact_id]['name'] = new_name
    
    # Get and validate new phone number (or keep current)
    while True:
        new_phone = input(f"New phone [{contacts[contact_id]['phone']}]: ").strip()
        if not new_phone:
            break  # Keep current phone
        if validate_phone(new_phone):
            contacts[contact_id]['phone'] = new_phone
            break
        print("❌ Invalid phone number. Please try again.")
    
    # Get and validate new email (or keep current)
    while True:
        new_email = input(f"New email [{contacts[contact_id]['email']}]: ").strip()
        if not new_email:
            break  # Keep current email
        if validate_email(new_email):
            contacts[contact_id]['email'] = new_email
            break
        print("❌ Invalid email format. Please try again.")
    
    # Save changes
    if save_contacts(contacts):
        print(f"\n✅ Contact updated successfully!")
    else:
        print("\n❌ Failed to save changes.")
    
    return contacts


def delete_contact(contacts):
    """
    Delete a contact from the contact list.
    
    Args:
        contacts (dict): Dictionary containing all contacts
    
    Returns:
        dict: Updated contacts dictionary
    """
    display_header("DELETE CONTACT")
    
    if not contacts:
        print("\n📭 No contacts available to delete.")
        return contacts
    
    # Display all contacts
    print(f"\n{'ID':<5} {'Name':<20} {'Phone':<18}")
    print("-"*45)
    for contact_id, contact_info in contacts.items():
        print(f"{contact_id:<5} {contact_info['name']:<20} {contact_info['phone']:<18}")
    
    # Get contact ID to delete
    contact_id = input("\nEnter the ID of the contact to delete: ").strip()
    
    # Check if contact exists
    if contact_id not in contacts:
        print(f"❌ Contact with ID '{contact_id}' not found.")
        return contacts
    
    # Confirm deletion
    contact_name = contacts[contact_id]['name']
    confirmation = input(f"\n⚠️  Are you sure you want to delete '{contact_name}'? (yes/no): ").strip().lower()
    
    if confirmation in ['yes', 'y']:
        # Delete the contact
        del contacts[contact_id]
        
        # Save changes
        if save_contacts(contacts):
            print(f"\n✅ Contact '{contact_name}' deleted successfully!")
        else:
            print("\n❌ Failed to save changes.")
    else:
        print("\n❌ Deletion cancelled.")
    
    return contacts


def get_menu_choice():
    """
    Get and validate the user's menu choice.
    
    Returns:
        str: Valid menu choice (1-6)
    """
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        
        print("❌ Invalid choice. Please enter a number between 1 and 6.\n")


def main():
    """
    Main function to run the Contact Management System.
    Displays menu and handles user choices.
    """
    # Display welcome message
    print("\n" + "="*60)
    print("  WELCOME TO SIMPLE CONTACT MANAGEMENT SYSTEM")
    print("="*60)
    print("\n📱 Manage your contacts efficiently!")
    print("💾 All changes are automatically saved to file.")
    
    # Load existing contacts from file
    contacts = load_contacts()
    
    if contacts:
        print(f"\n✅ Loaded {len(contacts)} existing contact(s).")
    
    # Main program loop
    while True:
        # Display menu
        display_menu()
        
        # Get user choice
        choice = get_menu_choice()
        
        # Execute appropriate function based on choice
        if choice == '1':
            # Add new contact
            contacts = add_contact(contacts)
        
        elif choice == '2':
            # View all contacts
            view_all_contacts(contacts)
        
        elif choice == '3':
            # Search contact
            search_contact(contacts)
        
        elif choice == '4':
            # Edit contact
            contacts = edit_contact(contacts)
        
        elif choice == '5':
            # Delete contact
            contacts = delete_contact(contacts)
        
        elif choice == '6':
            # Exit the program
            display_header("THANK YOU!")
            print("\n👋 Thanks for using the Contact Management System!")
            print("💾 All your contacts have been saved.\n")
            print("="*60 + "\n")
            break
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")


# Entry point of the program
if __name__ == "__main__":
    main()
