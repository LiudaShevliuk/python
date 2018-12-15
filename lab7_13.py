#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input_first_str() -> str:
    return input('Enter the first line: ')

def ui_input_second_str() -> str:
    return input('Enter the second line: ')

def ui_output(res: bool) -> None:
    if res:
        print('Yes, you can!')
    else:
        print('No, you can\'t!')

def checking(f_str: str, s_str: str) -> bool:
    return set(s_str).issubset(f_str)

ui_output(checking(ui_input_first_str(), ui_input_second_str()))
