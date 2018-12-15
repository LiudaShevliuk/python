#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def ui_input() -> str:
    return input('Enter your email for checking: ')

def ui_output(res: bool) -> None:
    if res:
        print('Good email!')
    else:
        print('Wrong email!')

def checking(email: str) -> bool:
    return re.match('^[\w.+\-]+@[\w]+\.[a-z]{2,3}$', email)

ui_output(checking(ui_input()))

