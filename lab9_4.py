#!/usr/bin/env python3
# -*- coding: utf-8 -*-

arabic = int(input("Enter arabic number: "))
roman = str(input("Enter roman number: "))


def to_roman_num(arabic_num: int) -> str:

    thousands_symb = ["", "M", "MM", "MMM"] 
    hundreds_symb = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens_symb = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]   
    ones_symb = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    thousands = thousands_symb[arabic_num // 1000]
    hundreds = hundreds_symb[arabic_num // 100 % 10]
    tens = tens_symb[arabic_num // 10 % 10]
    ones = ones_symb[arabic_num % 10]

    return thousands + hundreds + tens + ones


def to_arabic_num(roman_num: str) -> int:
    roman_num = roman_num.upper()

    numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    arabic_num = 0
    count = len(roman_num)

    for i in range(count):
        if i < count - 1 and numbers[roman_num[i]] < numbers[roman_num[i + 1]]:
            continue
        elif i > 0 and numbers[roman_num[i - 1]] < numbers[roman_num[i]]:
            arabic_num += numbers[roman_num[i]] - numbers[roman_num[i - 1]]
        else:
            arabic_num += numbers[roman_num[i]]

    return arabic_num


print('{} = {}'.format(arabic, to_roman_num(arabic)))
print('{} = {}'.format(roman, to_arabic_num(roman)))
