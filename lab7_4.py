#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def ui_input() -> str:
    """This function takes initial string"""
    return input('Enter your string: ')

def encription(string: str) -> str:
    """This function encrypts the string""" 
    res_string = str()
    for smbl in string:
        if smbl == 'z':
            res_string += 'a'
        elif smbl == 'Z':
            res_string += 'A'
        else:
            res_string += chr(ord(smbl)+1)
    return res_string

def ui_output(string: str) -> None:
    """This function print encrypted string"""
    print(string)

ui_output(encription(ui_input()))
