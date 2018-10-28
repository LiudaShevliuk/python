#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num = [8,16,5,3,9,1]

def selection_sort(initial_list: list) -> list:
    """This function does selection sort for the list""" 
    for i in range(len(initial_list)):
        min_pos = i
        for j in range(i+1, len(initial_list)):
            if initial_list[min_pos] > initial_list[j]:
                min_pos = j
        temp = initial_list[i]
        initial_list[i] = initial_list[min_pos]
        initial_list[min_pos] = temp
    return initial_list

def ui_output(sorted_list: list) -> None:
    """This function prints sorted list"""
    print('Sorted list: ', sorted_list)

ui_output(selection_sort(num))
