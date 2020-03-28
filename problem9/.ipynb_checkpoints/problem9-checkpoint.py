#!/bin/env/python
#-*- encoding: utf-8 -*-
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from __future__ import print_function, division
import math


def main():
    # Exhaustive Search, not ideal...
    exit = False
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = math.sqrt(a**2+b**2)
            if c % 1 == 0.0:
                if (a+b+c == 1000):
                    exit = True
                    break
        if exit == True:
            break
    print("Result: {}".format(int(a*b*c)))
    
    
if __name__ == "__main__":
    main()
