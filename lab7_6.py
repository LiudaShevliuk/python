#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    """This function takes entered string"""
    return input('Enter your string: ')

def star_frame(string: str) -> str:
    """This function does star frame around entered string"""
    return f'{"*" * (len(string)+4)}\n* {string} *\n{"*" * (len(string)+4)}'

print(star_frame(ui_input()))
