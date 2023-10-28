"""
This is a simple contact management bot.

It allows users to add, change, and view contact information.

"""

def input_error(func):
    """
    A decorator to handle common input errors and provide error messages.

    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter a valid name."
        except IndexError:
            return "Command requires more arguments."
    return inner

def parse_input(user_input):
    """
    Parse user input into a command and arguments.

    """
    cmd, *args = user_input.strip().lower().split()
    cmd = cmd.strip().lower()
    return cmd, *args

def is_valid_name(name, contacts):
    """
    Check if a contact name exists in the contacts.

    """
    if name not in contacts:
        raise KeyError("Contact not found.")
    return name

def is_valid_contact(name, contacts):
    """
    Check if a contact name already exists in the contacts.

    """
    if name in contacts:
        raise ValueError("Contact already exists.")
    return name

@input_error
def add_contact(args, contacts):
    """
    Add a contact to the contacts dictionary.

    """
    name, phone = args
    is_valid_contact(name, contacts)
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """
    Change the phone number of an existing contact.

    """
    name, new_phone = args
    is_valid_name(name, contacts)
    contacts[name] = new_phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    """
    Show the phone number of an existing contact.

    """
    if not args:
        raise IndexError("Command requires a name argument.")

    name = args[0]
    return contacts.get(name, "Contact not found")

def show_all(contacts):
    """
    Generate a string containing all contacts and their phone numbers.

    """
    contacts_str = ""
    for name, phone in contacts.items():
        contacts_str += f"{name}: {phone}\n"
    return contacts_str.rstrip()

def main():
    """
    The main function to run the contact management bot.

    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
