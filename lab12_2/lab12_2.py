#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Star:
    def __init__(self, name, x = 0, y = 0):
        self.name = name
        self.x = x
        self.y = y

    def rotate(self, angle):
        rad = angle * (math.pi / 180)
        self.x = self.x * math.cos(rad) - self.y * math.sin(rad)
        self.y = self.x * math.sin(rad) + self.y * math.cos(rad)

    def __gt__(self, star):
        if self.y != star.y:
            return self.y > star.y
        else:
            return self.x > star.x

    def __str__(self) -> str:
        return "%s %.2f %.2f" % (self.name ,self.x, self.y)

f = open('stars.txt', 'r+t', encoding='utf-8')

first_line = f.readline().split()
num_of_stars = int(first_line[0])
angle = int(first_line[1])
stars = []

for line in f:
    data = line.split()
    stars.append(Star(data[0], float(data[1]), float(data[2])))

f.close()

for star in stars:
    star.rotate(angle)

stars.sort()

f = open('result.txt', 'wt', encoding='utf-8')
f.write(' '.join(map(str, (star.name for star in stars))))
f.flush()
f.close()
