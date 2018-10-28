#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    """This function takes the text"""
    return input('Enter your text: ')

def morze_convertation(text: str) -> str:
    """This function converts text into Morze code"""
    m_alp = {'a': '.-', 'b': '-...', 'c': '-.-.',
             'd': '-..', 'e': '.', 'f': '..-.',
             'g': '--.', 'h': '....', 'i': '..',
             'j': '.---', 'k': '-.-', 'l': '.-..',
             'm': '--', 'n': '-.', 'o': '---',
             'p': '.--.', 'q': '--.-', 'r': '.-.',
             's': '...', 't': '-', 'u': '..-',
             'v': '...-', 'w': '.--', 'x': '-..-',
             'y': '-.--', 'z': '--..',

             '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.',
             '0': '-----',

             ' ': '   '
            }
    return ''.join(m_alp.get(i.lower()) for i in text)

def ui_output(morze_text: str) -> None:
    """This function prints converted text"""
    print(morze_text)

ui_output(morze_convertation(ui_input()))
