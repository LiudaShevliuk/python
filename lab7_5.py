#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def ui_input() -> str:
    """This function takes the string"""
    return input('Enter your string: ')

def count_vowels(string: str) -> int:
    """This function counts vowels"""
    vowels = ['a','o','u','i','e','y']
    count = 0
    for _ in vowels:
        count += string.count(_)
    return count

print(count_vowels(ui_input()))
