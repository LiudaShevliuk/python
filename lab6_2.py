#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def ui_input() -> list:
    """This function takes initial deposit, percentages and duration""" 
    print('Enter initial deposit, percentages and duration')
    return [int(input()), int(input()), int(input())]

def calc_deposit(param: list) -> float:
    """This function calculates the final deposit"""
    deposit = param[0] * (1 + (param[1])/100)**param[2]
    return deposit

def ui_output(deposit: float) -> None:
    """This function prints the final deposit"""
    print('Your deposit: {:.2f}'.format(deposit))

ui_output(calc_deposit(ui_input()))
