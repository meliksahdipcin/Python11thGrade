#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:25:24 2021

@author: meliksahdipcin
"""

class Employer:
    wageRatio = 1.8
    counter = 0
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name + surname + "@anabilim.k12.tr"
        
        Employer.counter = Employer.counter + 1
        
    def giveNameSurname(self):
        return self.name + " " + self.surname
    
    def rise(self):
        self.salary = self.salary + self.salary * self.wageRatio
        
employer1 = Employer("Jeff", "Bezos", 100000)
print("Employer's name: ", employer1.giveNameSurname())
print("Employer's first salery (USD): ", employer1.salary)
employer1.rise()
print("Employer's new salary (USD): ", employer1.salary)

employer2 = Employer("Elon", "Musk", 75000)
employer3 = Employer("Tim", "Cook", 50000)
employer4 = Employer("Craig", "Federighi", 35000)
employer5 = Employer("Bill", "Gates", 70000)

list = [employer1, employer2, employer3, employer4, employer5]
maxSalary = -1
index = -1
for each in list:
    if each.salary > maxSalary:
        maxSalary = each.salary
        index = each
        
print(maxSalary)
print(index.giveNameSurname())