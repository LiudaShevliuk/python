#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math
import cmath

print('Enter a, b, c: ')

a = float(input())
b = float(input())
c = float(input())

if a != 0 and b != 0 and c != 0:
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / 2*a
        x2 = (-b - math.sqrt(D)) / 2*a
        print('Solution: ', x1, x2)
    elif D == 0:
        x = -b / 2*a
        print('Solution: ', x)
    else:
        x1 = complex((-b + cmath.sqrt(D)) / 2*a)
        x2 = complex((-b - cmath.sqrt(D)) / 2*a)
        print('Solution: ', x1, x2)
elif (a == 0 and b != 0 and c == 0) or (a != 0 and b == 0 and c == 0):
    print('Solution: x = 0')
elif a == 0 and b == 0 and c != 0:
    print('It is no solution')
elif a == 0 and b == 0 and c == 0:
    print('Solution: x є R')
elif a == 0 and b != 0 and c != 0:
    x = -c / b
    print('Solution: ', x)
elif a != 0 and b != 0 and c == 0:
    x1 = 0
    x2 = -b / a
    print('Solution: ', x1, x2)
else:
    if (a > 0 and c > 0) or (a < 0 and c < 0):
        x1 = complex(-cmath.sqrt(-c/a))
        x2 = complex(cmath.sqrt(-c/a))
    else:
        x1 = -math.sqrt(-c/a)
        x2 = math.sqrt(-c/a)
    print('Solution: ', x1, x2)
