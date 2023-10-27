"""
This module contains classes for managing an address book.
"""

from collections import UserDict


class Field:
    """
    Base class for fields in a record.
    """

    def __init__(self, value):
        """
        Initialize a field with a value.
        """
        self.value = value


    def __str__(self):
        """
        Return the string representation of the field.
        """
        return str(self.value)


class Name(Field):
    """
    Class for storing contact names.
    """

    def __init__(self, value):
        """
        Initialize a name field.
        """
        super().__init__(value)


class Phone(Field):
    """
    Class for storing phone numbers with validation.
    """


    def __init__(self, value):
        """
        Initialize a phone field with validation.
        """
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number format. Please provide 10 digits.")
        self.value = value


    @staticmethod
    def validate_phone(phone):
        """
        Validate the phone number format.
        """
        return phone.isdigit() and len(phone) == 10


class Record:
    """
    Class for storing contact information, including name and a list of phones.
    """


    def __init__(self, name):
        """
        Initialize a record with a name and an empty list of phones.
        """
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
        """
        Add a phone number to the record.
        """
        self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        """
        Remove a phone number from the record.
        """
        self.phones = [p for p in self.phones if str(p) != phone]


    def find_phone(self, phone):
        """
        Find a phone number in the record.
        """
        for p in self.phones:
            if str(p) == phone:
                return str(p)
        return None


    def __str__(self):
        """
        Return a string representation of the record.
        """
        phones_str = "; ".join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


    def get_phones(self):
        """
        Get the list of phone numbers.
        """
        return [str(phone) for phone in self.phones]


class AddressBook(UserDict):
    """
    Class for managing records in an address book.
    """


    def add_record(self, record):
        """
        Add a record to the address book.
        """
        self.data[record.name.value] = record


    def find(self, name):
        """
        Find a record in the address book by name.
        """
        return self.data.get(name)


    def delete(self, name):
        """
        Delete a record from the address book by name.
        """
        if name in self.data:
            del self.data[name]


    def get_all_records(self):
        """
        Get all records in the address book.
        """
        return list(self.data.values())


if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for record in book.get_all_records():
        print(record)

    john = book.find("John")
    john.remove_phone("1234567890")
    john.add_phone("1112223333")
    print(john)

    found_phone = john.find_phone("5555555555")
    if found_phone:
        print(f"{john.name.value}: {found_phone}")

    book.delete("Jane")
