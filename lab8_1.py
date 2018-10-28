#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input_num() -> int:
    """This function takes number of people"""
    return int(input('Enter number of people: '))

def ui_input_step() -> int:
    """This function takes the step"""
    return int(input('Enter the step: '))

def survived(num_people: int, step: int) -> list:
    """This function defines survived person"""
    people = list(range(1, num_people+1))
    position = 0
    while len(people) > 1:
        position += 1
        person = people.pop(0)
        if position != step:
            people.append(person)
        else:
            position = 0
    return people

def ui_output(survived: list) -> None:
    """This function prints the number of survived person"""
    print('Survived: ', survived)

ui_output(survived(ui_input_num(), ui_input_step()))
