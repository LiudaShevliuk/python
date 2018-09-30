#!/usr/bin/env python3
# -*- coding:utf-8 -*-

num = int(input('Enter positive number: '))

if num <= 0:
    print('Wrong number!')
    exit()

i = 2
j = 0

while i**2 <= num and j != 1:
    if num % i == 0:
        j = 1
    i += 1

if j == 1:
    print('It\'s a composite number')
else:
    print('It\'s a prime number ')
