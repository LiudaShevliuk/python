#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    """This function takes the ticket number"""
    return input("Input your ticket number: ")

def ui_output(result: bool) -> None:
    """This function prints the result of checking"""
    if result:
        print("You have a lucky ticket!")
    else:
        print("Your ticket is unlucky")

def is_lucky(num_of_ticket: str) -> bool:
    """This function checks if the number of ticket is lucky"""
    half_num = int(len(num_of_ticket) / 2)
    num_of_ticket = list(map(int, num_of_ticket))
    return sum(num_of_ticket[:half_num]) == sum(num_of_ticket[half_num:])

ui_output(is_lucky(ui_input()))
