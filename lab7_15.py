#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
import random

def ui_output(password: str) -> None:
    print('Your password: ', password)

def generate_pswd() -> str:
    letters = [random.choice(string.ascii_letters) for _ in range(8)]
    number = random.choice(string.digits)
    symbol = random.choice(string.punctuation)
    pswd = letters + list(number) + list(symbol)
    random.shuffle(pswd)
    return ''.join(pswd)

ui_output(generate_pswd())
