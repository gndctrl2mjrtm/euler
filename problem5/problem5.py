#!/bin/env/python
#-*- encoding: utf-8 -*-
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from __future__ import print_function, division


def main():
    factors = list(range(20, 1, -1))
    i = 60
    while True:
        valid = True
        for f in factors:
            if i % f != 0:
                valid = False
                break
        if valid:
            break
        else:
            i += 1
    
    print("Result: {}".format(i))
    
    
if __name__ == "__main__":
    main()