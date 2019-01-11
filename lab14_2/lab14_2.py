#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read_info(file):
    while True:
        data = file.readline();
        if not data:
            break
        yield data

class Contact:
    def __init__(self, first_name = '', last_name = '', number = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number

    def __str__(self) -> str:
        return "{} {}: {}".format (self.first_name, self.last_name, self.number)

    def __gt__(self, another_contact):
        if self.last_name != another_contact.last_name:
            return self.last_name.__gt__(another_contact.last_name)
        else:
            return self.first_name.__gt__(another_contact.first_name)

    def add_from_console(self):
        self.first_name = input('Enter first name: ')
        self.last_name = input('Enter last name: ')
        self.number = input('Enter phone number: ')

    def __eq__(self, o: object) -> bool:
        return self.number == o.number

    def update(self, property):
        try:
            setattr(self, property, input("Enter " + property + ": "))
        except:
            print('Invalid property')


class PhoneBook:
    def __init__(self):
        self.records = []
        try:
            f = open('./phone_book.txt')
            for line in read_info(f):
                args = line.split()
                self.records.append(Contact(args[0], args[1], args[2]))
            f.close()
        except Exception as e:
            print("Something wrong!\n" + str(e))

    def add_to_file(self):
        f = open('./phone_book.txt', 'wt', encoding='utf-8')
        for item in self.records:
            f.write('{} {} {}\n'.format(item.first_name, item.last_name, item.number))
        f.flush()
        f.close()

    def add(self):
        record = Contact()
        record.add_from_console()
        self.records.append(record)

    def remove_by_id(self, id):
        self.records.pop(int(id))

    def search_by_name(self, name):
        result = ''
        for item in self.records:
            if (item.first_name + " " + item.last_name).__contains__(name):
                result += '{}\n'.format(item)
        return result

    def update(self, id):
        property = input('Enter property name (first_name, last_name, number): ')
        self.records[int(id)].update(property)

    def __str__(self) -> str:
        result = ''
        for idx, val in enumerate(self.records):
            result += '{} - {}\n'.format(idx, val)
        return result


phone_book = PhoneBook()
while True:
    action = input("1 - Add contact\n2 - Remove by id\n3 - Show contacts\n"
                   "4 - Update contact\n5 - Search by name\n6 - Exit\n")
    try:
        if action == '1':
            phone_book.add()
        elif action == '2':
            phone_book.remove_by_id(input('Enter id: '))
        elif action == '3':
            print(phone_book)
        elif action == '4':
            phone_book.update(input('Enter id: '))
        elif action == '5':
            print(phone_book.search_by_name(input('Enter name: ')))
        elif action == '6':
            phone_book.add_to_file()
            break
    except Exception as e:
        print("Something wrong!\n" + str(e))
