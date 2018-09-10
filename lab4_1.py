#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

a = float(input('Enter positive number: '))
b = float(input('Enter one more positive number that  greater than 0: '))

x = math.sqrt(a * b) / (math.exp(a) * b) + a* math.exp(2 * a / b)

print(x)
