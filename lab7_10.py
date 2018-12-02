#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    return input('Enter your text: ')

def ui_output(sm_word: str) -> None:
    print("The smallest word: ", sm_word)

def find_the_smallest_word(text: str) -> str:
    return min(text.split())

ui_output(find_the_smallest_word(ui_input()))
