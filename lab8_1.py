#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input_num() -> int:
    return int(input('Enter number of people: '))

def ui_input_step() -> int:
    return int(input('Enter the step: '))

def survived(num_people: int, step: int) -> list:
    people = list(range(1, num_people+1))
    position = 0

    while len(people) > 1:
        position += 1
        human = people.pop(0)
        if position != step:
            people.append(human)
        else:
            position = 0
    return people

def ui_output(survived: list) -> None:
    print('Survived: ', survived)

ui_output(survived(ui_input_num(), ui_input_step()))
