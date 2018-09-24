#!/usr/bin/env python3
# -*- coding:utf-8 -*-

print('Enter the sides of triangle: ')

a = int(input())
b = int(input())
c = int(input())

if a < 1 or b < 1 or c < 1:
    print('Wrong sides!')
    exit()

if a + b > c and a + c > b and b + c > a:
    print('Triangle exists')
else:
    print('Triangle doesn\'t exist')
