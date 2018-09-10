#!/usr/bin/env python3
# -*- coding: utf-8 -*-

weight = float(input('Enter your weight: '))
height = float(input('Enter your height in meters: '))

bmi = weight / height**2

print('Your BMI = ', bmi)
