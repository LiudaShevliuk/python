#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

player = int(input('Choose: 1-rock, 2-scissors, 3-paper: '))

if player > 3 or player < 1:
    print('Your choice is wrong')
    exit()

comp = random.randint(1,3)

print('Your choice - ', player, ', Computer\'s  choice - ', comp) 

if player == comp:
    print('Draw')
elif (player == 1 and comp == 3) or (player == 2 and comp == 1) or \
(player == 3 and comp == 2):
    print('Computer win')
else:
    print('Player win')
