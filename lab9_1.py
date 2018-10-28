#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> str:
    """This function takes player's cards"""
    return input('Enter all your cards (with spaces): ')

def blackjack(cards: str) -> int:
    """This function counts points"""
    cards_values = { '2': 2, '3': 3, '4': 4,
                     '5': 5, '6': 6, '7': 7,
                     '8': 8, '9': 9, 'T': 10,
                     'J': 10, 'Q': 10, 'K': 10
                   }
    a_num = 0
    points = 0
    for card in cards.split():
        if card in cards_values:
            points = points + cards_values[card]
        elif card == 'A':
            a_num = a_num + 1

    if a_num > 0:
        for _ in  range(a_num):
            if a_num > 1:
                points = points + 1
                a_num = a_num - 1
            else:
                if points + 11 < 22:
                    points = points + 11
                else: 
                    points = points + 1

    return points

def ui_output(points: int) -> None:
    """This function prints the result"""
    if points <= 21:
        print('Your points: ', points)
    else:
        print('Bust')

ui_output(blackjack(ui_input()))
