#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

def ui_input() -> list:
    """This function takes three sides of trisngle"""
    print('Enter three sides of triangle: ')
    sides = [int(input()), int(input()), int(input())]
    return sides

def triangle_square(sides: list) -> float:
    """This function calculates square of the triange"""
    half_per = (sides[0]+sides[1]+sides[2]) / 2
    square = math.sqrt(half_per * (half_per-sides[0]) * (half_per-sides[1]) \
    * (half_per-sides[2]))
    return square

def ui_output(square: float) -> None:
    """This function print  the square of triangle"""
    print('Square: {:1.3f}'.format(square))

sides = ui_input()
square = triangle_square(sides)
ui_output(square)

