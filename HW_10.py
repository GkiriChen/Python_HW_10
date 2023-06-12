from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass


class Phone(Field):
    pass

class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        if phone:
            self.phones = []
            self.phones.append(phone)

    def add_phone(self):
        pass

    def del_phone(self):
        pass

    def editing_phone(self):
        pass


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


if __name__ == "__main__":
    name = Name('gena')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['gena'], Record)
    assert isinstance(ab['gena'].name, Name)
    assert isinstance(ab['gena'].phones, list)
    assert isinstance(ab['gena'].phones[0], Phone)
    assert ab['gena'].phones[0].value == '1234567890'
    print('All Ok)')