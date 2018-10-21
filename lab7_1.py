#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def offset_of_str(string: str, offset: int) -> str:
    """This function does the offset of string""" 
    res_string = string[offset:] + string[:offset]
    return res_string

def ui_output(res: str) -> None:
    """This function print an offset string"""
    print(res)

ui_output(offset_of_str(input('Enter your string: '),\
          int(input('Enter the offset: '))))
