#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import timeit

def power_by_shift() -> int:
    return 2 << 49

def power_by_operator() -> int:
    return 2 ** 50

def power_by_pow() -> int:
    return pow(2, 50)

def power_by_math_pow() -> int:
    return math.pow(2, 50)

def revers_by_map(strings: list) -> list:
    return list(map(lambda x: x[::-1], strings))

def revers_by_comprehension(strings: list) -> list:
    result = []
    result += [string[::-1] for string in strings]
    return result

def revers_by_for(strings: list) -> list:
    result = []
    for string in strings:
        string = string[::-1]
        result.append(string)
    return result

def timeit_shift() -> float:
    return timeit.timeit('power_by_shift()', \
           setup = "from __main__ import power_by_shift", \
           number = 10000)

def timeit_operator() -> float:
    return timeit.timeit('power_by_operator()', \
           setup = "from __main__ import power_by_operator", \
           number = 10000)

def timeit_pow() -> float:
    return timeit.timeit('power_by_pow()', \
           setup = "from __main__ import power_by_pow", \
           number = 10000)

def timeit_math_pow() -> float:
    return timeit.timeit('power_by_math_pow()', \
           setup = "from __main__ import power_by_math_pow", \
           number = 10000)

def timeit_map() -> float: 
    return timeit.timeit('revers_by_map(strings)', \
        setup = 'from __main__ import revers_by_map; \
	strings = [ \
        	"qwerty", "python", "123", "qwerty", "python", "123", \
        	"qwerty", "python", "123", "qwerty", "python", "123", \
        	"qwerty", "python", "123", "qwerty", "python", "123", \
        	]', \
        number = 10000)

def timeit_comprehension() -> float:
    return timeit.timeit('revers_by_comprehension(strings)', \
        setup = 'from __main__ import revers_by_comprehension; \
	strings = [ \
        	"qwerty", "python", "123", "qwerty", "python", "123", \
        	"qwerty", "python", "123", "qwerty", "python", "123", \
        	"qwerty", "python", "123", "qwerty", "python", "123", \
        	]', \
        number = 10000)

def timeit_for_loop() -> float:
    return timeit.timeit('revers_by_for(strings)', \
        setup = 'from __main__ import revers_by_for; \
	strings = [ \
        	"qwerty", "python", "123", "qwerty", "python", "123", \
        	"qwerty", "python", "123", "qwerty", "python", "123", \
        	"qwerty", "python", "123", "qwerty", "python", "123", \
        	]', \
        number = 10000)

def ui_output(shift_time: float, operator_time: float, pow_time: float, \
              math_pow_time: float, map_time: float, comp_time: float, \
              for_time: float,) -> None:
    print("Shift time is", shift_time)
    print("** operator time is", operator_time)
    print("Pow() time is", pow_time)
    print("Math.pow() time is", math_pow_time)
    print("Map() time is", map_time)
    print("Comprehension time is", comp_time)
    print("For time is", for_time)

ui_output(timeit_shift(), timeit_operator(), timeit_pow(), \
          timeit_math_pow(), timeit_map(), timeit_comprehension(), \
          timeit_for_loop())
