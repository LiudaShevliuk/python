#!/usr/bin/env python3
# -*- coding:utf-8 -*-

input_string = input('Enter your string: ')
offset = int(input('Enter the offset: '))

if offset > len(input_string)/2:
    print('Enter another offset!')
    exit()

res_string = input_string[offset:] + input_string[:offset]

print(res_string)

