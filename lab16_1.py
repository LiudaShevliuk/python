#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.codeabbey.com/index/user_ranking").content
soup = BeautifulSoup(html, 'html.parser')

table = soup.find_all('tr')

with open('ranking.csv', 'w') as f:
    f.write('position,username,language,rank,enlightenment,solved\n')

    for row in table[2:]:
        res = row.get_text().split()
        res = [_.replace(',', '') for _ in res]
        res = ','.join(res)
        f.write(res + '\n')
