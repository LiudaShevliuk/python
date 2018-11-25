#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import abc
import random

class Employee:
    @abc.abstractmethod
    def calc_salary(self):
        return

    @abc.abstractmethod
    def calc_tax(self):
        return

class HourlyEmployee(Employee):
    def __init__(self, name: str, hourly_rate: int) -> None:
        self.name = name
        self.hourly_rate = hourly_rate

    def calc_salary(self) -> float:
        return 20.8 * 8 * self.hourly_rate

    def calc_tax(self) -> float:
        return self.calc_salary() * 0.18 + self.calc_salary() * 0.015

class MonthlyEmployee(Employee):
    def __init__(self, name: str, monthly_rate: int) -> None:
        self.name = name
        self.monthly_rate = monthly_rate

    def calc_salary(self) -> int:
        return self.monthly_rate

    def calc_tax(self) -> float:
        return self.calc_salary() * 0.18 + self.calc_salary() * 0.015

class Entrepreneur(Employee):
    def __init__(self, name: str, hourly_rate: int) -> None:
        self.name = name
        self.hourly_rate = hourly_rate

    def calc_salary(self) -> float:
        return 20.8 * 8 * self.hourly_rate * 1.1

    def calc_tax(self) -> float:
        return self.calc_salary() * 0.05 + 704

class Freelancer(Employee):
    def __init__(self, name: str, line_rate: int, num_of_lines: int) -> None:
        self.name = name
        self.line_rate = line_rate
        self.num_of_lines = num_of_lines

    def calc_salary(self) -> float:
        return self.line_rate * self.num_of_lines

    def calc_tax(self) -> float:
        return self.calc_salary() * 0.18 + self.calc_salary() * 0.015 + 704

def employees_creating() -> list:
    names = ('Liuda', 'Tania', 'Vlad', 'Andrii', 'Vasia', 'Serhii', 'Taras')
    employees = []
    for _ in range(5):
        name = random.choice(names)
        employees.append(random.choice([
             HourlyEmployee(name, random.randint(100, 500)),
             MonthlyEmployee(name, random.randint(10000, 25000)),
             Entrepreneur(name, random.randint(100, 500)),
             Freelancer(name, random.randint(10, 50), random.randint(500, 5000))
             ]))
    return sorted(employees, key=lambda x: x.calc_salary(), reverse=True)

def ui_output(employees: list) -> None:
    for employee in employees:
        print('Employee:', employee.name, ' Salary:', employee.calc_salary(), ' Tax:',
               employee.calc_tax(), '\n')

ui_output(employees_creating())
