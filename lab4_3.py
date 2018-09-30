#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import decimal

income = decimal.Decimal(input('Enter your income: '))

tax = income * decimal.Decimal('0.18')
military_tax = income * decimal.Decimal('0.015')
all_tax = decimal.Decimal(tax) + decimal.Decimal(military_tax)

print('Tax = ', tax, 'Military tax = ', military_tax)
print('All tax = ', all_tax)
