#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4
import requests
import csv
import re

def formatting(value: str) -> str:
    return value.replace("\'", '').replace("\"", '').replace("\n", ' ')

def write_info(web_page, writer) -> None:
    soup = bs4.BeautifulSoup(web_page.content, 'html.parser')
    laptops = soup.find_all(class_ = 'product-block')

    for laptop in laptops:
        name = laptop.find(class_ = 'model-name').text
        price = laptop.find(class_ = 'price').text
        all_desc = laptop.find_all(class_ = 'short-descr-line')
        description = '\n'.join([description.text.strip() for description in all_desc])
        link = laptop.find(class_ = 'btn')['href']
        if link[0] == '/':
            link = "https://price.ua" + link
        img_link = laptop.find(class_ = 'photo-wrap').find('img')['src']
        img_link = f"https:{img_link}"
        writer.writerow([formatting(name),
                         formatting(price),
                         formatting(description),
                         formatting(link),
                         formatting(img_link)])

url = "https://price.ua/catc839t14/page{}.html?price[min]=10000&price[max]=20000"
i = 1

with open("laptops.csv", 'w', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    while True:
        info = requests.get(url = url.format(i))
        page = int(re.search(r'page\d+', info.url).group(0).replace('page', '')) \
            if i != 1 else 1
        if i != page:
            break
        else: 
            write_info(info, writer)
            i += 1
