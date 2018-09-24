#!/usr/bin/env python3
# -*- coding:utf-8 -*-

print('Enter the height and the width dimensions of the rectangular door:')

h = int(input())
w = int(input())

print('Enter three dimensions of the box:')

a = int(input())
b = int(input())
c = int(input())

if a >= h and b <= w :
    print('Yes')
elif b <= h and a <= w:
    print('Yes')
elif b <= h and c <= w:
    print('Yes')
elif c <= h and b <= w:
    print('Yes')
elif a <= h and c <= w:
    print('Yes')
elif c <= h and a <= w:
    print('Yes')
else:
    print('No')  
