
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def ui_input() -> str:
    """This function takes the string"""
    return input('Enter your string: ')

def remove_symbols(string: str) -> str:
    """This function removes all symbols except brackets from string"""
    brackets = ['(', ')', '[', ']', '{', '}', '<', '>']
    for _ in string:
        if _ not in brackets:
            string = string.replace(_, '')
    return string

def remove_brackets_pairs(string: str) -> bool:
    """This function removes brackets pairs"""
    brackets_pairs = ['()','{}','[]','<>']
    while len(string) > 0:
        start_len = len(string)
        for _ in brackets_pairs:
            if _ in string:
                string = string.replace(_, '')
            if len(string) == 0:
                return True
        if start_len == len(string):
            break
    return False

print(remove_brackets_pairs(remove_symbols(ui_input())))
