#!/usr/bin/python

from math import factorial
#from multiprocessing import Pool

def print_factorial ():
    print('start calculating')
    return factorial(70000)

#if __name__ == '__main__':
#    with Pool(5) as p:
#        print(p.map(print_factorial, [50000, 60000, 70000]))
