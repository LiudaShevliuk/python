#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

class Record:
    def __init__(self, task='', deadline = datetime.datetime.now(), \
                 priority = 'normal', status = 'in process'):
        self.task = task
        self.deadline = deadline
        self.priority = priority
        self.status = status

    def __str__(self) -> str:
        return "{} {} {}; {}".format (self.task ,self.deadline, \
                                      self.priority, self.status)

    def __gt__(self, another_task):
        self.deadline.__gt__(another_task.deadline)

    def add_from_console(self):
        self.task = input('Add your task: ')
        date = input('Add date (dd/mm/yyyy): ')
        try:
            self.deadline = datetime.datetime.strptime(dt, '%d/%m/%Y')
        except:
            self.deadline = datetime.datetime()
        self.priority = input('Add priority: ')
        self.status = input('Add Status: ')

    def __eq__(self, o: object) -> bool:
        if o is not Record or self.task != o.task or \
            self.deadline != o.deadline or self.priority != o.priority\
            or self.status != o.status:
            return False
        else:
            return True

    def update(self, property):
        try:
            if property != 'deadline':
                setattr(self, property, input("Enter " + property + ": "))
            else:
                setattr(self, property, datetime.datetime.strptime( \
                        input("Enter " + property + "(dd/mm/yyyy): "), \
                        '%d/%m/%Y'))
        except:
            print('Invalid property!')


class ToDoList:
    def __init__(self):
        self.records = []

    def add(self):
        record = Record()
        record.add_from_console()
        self.records.append(record)

    def remove(self, obj):
        if obj is int or str(obj).isdigit():
            self.records.pop(int(obj))
        else:
            for item in self.records:
                if item.task == obj:
                    self.records.remove(item)

    def search_by_task(self, task):
        for item in self.records:
            if item.task == task:
                return item

    def mark_done(self, id):
        self.records[int(id)].status = 'Done!'

    def update(self, id):
        property = input('Enter property name (task, deadline, priority, status): ')
        self.records[int(id)].update(property)

    def __str__(self) -> str:
        result = ''
        for idx, val in enumerate(self.records):
            result += '{} - {}\n'.format(idx, val)
        return result


to_do_list = ToDoList()
to_do_list.records.append(Record('Send labs', datetime.datetime(2019, 1, 11), \
                                 'Must be done!', 'In process'))
to_do_list.records.append(Record('Read theory', datetime.datetime(2019, 1, 14),\
                           'High', 'In process'))

while True:
    action = input("1 - Add new task\n2 - Remove by id or task\n3 - Show tasks\n" \
                   "4 - Search by task\n5 - Mark as solved\n6 - Update\n" \
                   "7 - Exit\n")
    try:
        if action == '1':
            to_do_list.add()
        elif action == '2':
            to_do_list.remove(input('Enter id or task: '))
        elif action == '3':
            print(to_do_list)
        elif action == '4':
            print(to_do_list.search_by_task(input('Enter task: ')))
        elif action == '5':
            to_do_list.mark_done(input('Enter id: '))
        elif action == '6':
            to_do_list.update(input('Enter id: '))
        elif action == '7':
            break
    except Exception as e:
        print("Something wrong!\n" + str(e))
