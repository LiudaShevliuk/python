#!/usr/bin/env python3
# -*- coding:utf-8 -*-

string = input('Enter your string: ')

def remove_symbols(string):
    brackets = ['(', ')', '[', ']', '{', '}', '<', '>']
    for _ in string:
        if _ not in brackets:
            string = string.replace(_, '')
    return string

def remove_brackets_pairs(string):
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

brackers_str = remove_symbols(string)

if len(string) % 2 == 0:
    print(remove_brackets_pairs(brackers_str))
else:
    print('False')







