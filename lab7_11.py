#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    return input("Enter your text: ")

def ui_output(result: str) -> None:
    print("Sorted text: ", result)

def sorting_by_len(text: str) -> str:
    return ' '.join(sorted(text.split(), key = len))

ui_output(sorting_by_len(ui_input()))
