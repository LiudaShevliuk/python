#!/usr/bin/env python3
# -*- coding: utf-8 -*-

numbers = [1, 5, 8, 6, 10, 10]

def average(num: list) -> float:
    """This function calculates average of the list"""
    return sum(num) / len(num)

def median(num: list) -> float:
    """This function calculates median of the list"""
    length = len(num)
    num = sorted(num)
    if length%2 == 1:
        return num[length//2]
    else: 
        return (num[length//2-1] + num[length//2])/2

def ui_output(average: float, median: float) -> None:
    """This function prints list, average and median of the list"""
    print('List: ', numbers, '\nAverage:', average, '\nMedian: ', median)

ui_output(average(numbers), median(numbers))

