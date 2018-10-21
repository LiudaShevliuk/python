#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for _ in range(1,100):
    if _ % 15 == 0:
        print('FizzBuzz')
    elif _ % 3 == 0:
        print('Fizz')
    elif _ % 5 == 0:
        print('Buzz')
    else:
        print(_)
