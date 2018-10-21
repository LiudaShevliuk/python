#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def ui_input() -> str:
    """This function takes string for checking"""
    return input('Enter your phrase: ')

def is_palindrome(string: str) -> bool:
    """This function does all letters lowercase,\ 
       deletes all other symbols and checks if it\
       is a palindrome"""
    string = string.lower()
    symbols = [' ', '\'', '\"', '.', ',', ';', ':', '\\']
    res_string = []
    for _ in string:
        if _ not in symbols:
            res_string.append(_)  
    return res_string == res_string[::-1]

def ui_output(is_pal: bool) -> None:
    """This function prints the result of checking"""
    print(is_pal)

ui_output(is_palindrome(ui_input()))
