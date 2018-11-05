#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def random(seed = 654321):
    while True:
        x = str(seed)
        if len(x) != 6:
            x = (6 - len(x)) * '0' + x
        y = x[3:6] + x[0:3]
        res = str(int(x)*int(y))
        if len(res) != 12:
            res = (12 - len(res)) * '0' + res
        seed = res[3:9]
        yield int(seed)

func = random()
for _ in range(10):
    print(func.__next__())
