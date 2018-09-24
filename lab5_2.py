#!/usr/bin/env python3
# -*- coding:utf-8 -*-

print('Enter the height and the width dimensions of the rectangular door:')

h = int(input())
w = int(input())

print('Enter three dimensions of the box:')

a = int(input())
b = int(input())
c = int(input())

if (a <= h and b <= w) or (b <= h and a <= w) or (b <= h and c <= w) or \
(c <= h and b <= w) or (a <= h and c <= w) or (c <= h and a <= w) :
    print('Yes')
else:
    print('No')  

