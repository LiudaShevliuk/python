#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

print('Enter three numbers: ')

a = float(input())
b = float(input())
c = float(input())

function = math.exp(-(a-b)**2/(2*c**2)) / (c*math.sqrt(2*math.pi))

print('Result: ', function)

