#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    return input("Enter your text: ")

def ui_output(res_str: str) -> None:
    print("Result: ", res_str)

def del_extra_spaces(text: str) -> str:
    return ' '.join(text.split())

ui_output(del_extra_spaces(ui_input()))
