#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    return input('Enter your text: ')

def ui_choice() -> int:
    return int(input('Choose the case you want to make: 1 - camel case, 2 - snake case: '))

def ui_output(res: str) -> None:
    print(res)

def make_camel_case(text: str) -> str:
    res = str()
    next_low = False
    for smbl in text:
        if next_low:
            smbl = smbl.upper()
            next_low = False
        if smbl == '_':
            smbl = ''
            next_low = True
        res += smbl
    return res

def make_snake_case(text: str) -> str:
    res = str()
    for smbl in text:
        if smbl.isupper():
            smbl = '_' + smbl.lower()
        res += smbl
    return res

if ui_choice() == 1:
    ui_output(make_camel_case(ui_input()))
else:
    ui_output(make_snake_case(ui_input()))

