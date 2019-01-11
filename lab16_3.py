#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import html
import requests
import re
import csv

class School:
    def __init__(self, number, full_name, name, ownership, period, address, region) -> None:
        self.number = number
        self.full_name = full_name
        self.name = name
        self.ownership = ownership
        self.period = period
        self.address = address
        self.region = region

    def __str__(self) -> str:
        return "{},{},{},{},{},{},{}".format(self.number, self.full_name, self.name, self.ownership, self.period,
                                             self.address, self.region)

page = requests.get('https://if.isuo.org/authorities/schools-list/id/626')
tree = html.fromstring(page.content)
data = tree.xpath('//tr')
schools = []
first = data.pop(0)

for line in data:
    try:
        children = line.getchildren()
        schools.append(School(children[0].text_content().strip(), re.sub('\s+', '-',children[1].text_content().strip()),
                              children[2].text_content().strip(), children[3].text_content().strip(),
                              re.sub('\s+', '-', children[4].text_content().strip()), children[5].text_content().strip(),
                              children[6].text_content().strip()))
    except Exception as e:
        print(e)

with open("schools.csv", 'w', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    for school in schools:
        csv_writer.writerow([
                            school.number,
                            school.full_name,
                            school.name,
                            school.ownership,
                            school.period,
                            school.address,
                            school.region])
