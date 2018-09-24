#!/usr/bin/env python3
# -*- coding:utf-8 -*-

num = int(input('Enter your number: '))

if num & (num - 1):
    print('False')
else:
    print('True')




