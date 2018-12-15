#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_output(res: int) -> None:
    print('Byte size =' , res)

def parse_file(file: str) -> int:
    f = open(file, 'r')
    for line in f:
        bytes = line.split()[9]
        yield int(bytes)

def count_size(bytes: list) -> int:
    size = 0
    for byte in bytes:
        size += byte
    return size

ui_output(count_size(parse_file('2017_05_07_nginx.txt')))
