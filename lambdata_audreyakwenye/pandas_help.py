#!/usr/bin/env python
"""Python module for Schools/Teachers/Students 
"""

def letter_grade(num):
    if num > 95:
        print('A')
    elif num > 90:
        print('A-')
    elif num > 85:
        print('B')
    elif num > 80:
        print('B-')
    elif num > 75:
        print('C')
    elif num > 70:
        print('C-')
    elif num > 65:
        print('D')
    elif num > 60:
        print('D-')
    else:
        print('Failed')