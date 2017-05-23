#!/usr/bin/python

from math import factorial
from multiprocessing import Pool

def print_factorial (value):
    return factorial(value)

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(print_factorial, [50000, 60000, 70000]))
