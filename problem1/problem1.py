#!/bin/env/python
#-*- encoding: utf-8 -*-
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from __future__ import print_function, division


def main():
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print("Result: {}".format(total))
    
    
if __name__ == "__main__":
    main()