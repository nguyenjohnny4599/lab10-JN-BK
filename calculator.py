# https://github.com/nguyenjohnny4599/lab10-JN-BK
# Partner 1: Bogdan Krintal
# Partner 2: Johnny Nguyen

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math


def square_root(a): return math.sqrt(a)# raise ValueError if a < 0

def hypotenuse(a, b): return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError()
    return b / a

def logarithm(a,b):
    if a <= 0 or a == 1:
        raise ValueError()
    if b <= 0:
        raise ValueError()

    return math.log(b,a)

def exp(a,b):
    return a ** b



