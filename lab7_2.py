#!/usr/bin/env python3
# -*- coding:utf-8 -*-

phrase = input('Enter your phrase: ')

def isPalindrome(string):
    string = string.lower()
    symbols = [' ', '\'', '\"', '.', ',', ';', ':', '\\']
    res_string = []
    for _ in string:
        if _ not in symbols:
            res_string.append(_)
    return res_string == res_string[::-1]

print(isPalindrome(phrase))
