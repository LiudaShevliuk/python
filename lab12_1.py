#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "Point({},{})".format(self.x, self.y)

    def calc_distance(self, point) -> float:
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


class Triangle:
    def __init__(self, a = Point(), b = Point(), c = Point()):
        self.a = a
        self.b = b
        self.c = c

    def is_exist(self) -> bool:
        x = self.a.calc_distance(self.b)
        y = self.a.calc_distance(self.c)
        z = self.b.calc_distance(self.c)
        return x + y > z and x + z > y and y + z > x

    def calc_perimeter(self) -> float:
        x = self.a.calc_distance(self.b)
        y = self.a.calc_distance(self.c)
        z = self.b.calc_distance(self.c)
        return x + y + z

    def calc_square(self) -> float:
        x = self.a.calc_distance(self.b)
        y = self.a.calc_distance(self.c)
        z = self.b.calc_distance(self.c)
        p = (x + y + z) / 2
        return math.sqrt(p * (p - x) * (p - y) * (p - z))


first_point = Point()
second_point = Point(5, 8)
print("{} - {} = {}".format(first_point, second_point, first_point.calc_distance(second_point)))

a = Point(8, 3)
b = Point(3, 0)
c = Point(0, 4)

triangle = Triangle(a,b,c)
print("Does triangle exist?: {}".format(triangle.is_exist()))
print("Perimeter = {}, Square = {}".format(triangle.calc_perimeter(), triangle.calc_square()))
