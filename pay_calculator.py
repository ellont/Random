# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

str_hour = input('Hours worked:')
hour = float(str_hour)
rate = 10.5


if hour <= 40:
    pay = hour * rate
    print(pay)
else:
    pay = 40 * rate + (hour-40) * rate * 1.5
    print(pay)