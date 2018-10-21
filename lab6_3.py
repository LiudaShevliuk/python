#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

def ui_input() -> list:
    """This function takes initial deposit, final deposit and percentages""" 
    print('Enter initial deposit, final deposit and percentages')
    return [int(input()), int(input()), int(input())]

def calc_duration(param: list) -> float:
    """This function calculates the duration of deposit"""
    duration = math.log(param[1] / param[0], 1 + param[2]/100)
    return duration

def ui_output(duration: float) -> None:
    """This function prints the duration of deposit"""
    print('Duration: {:.2f}'.format(duration))

ui_output(calc_duration(ui_input()))
