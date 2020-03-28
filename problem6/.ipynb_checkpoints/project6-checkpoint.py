#!/bin/env/python
#-*- encoding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from __future__ import print_function, division


def main():
    # Boring way to do this, there are better mathematical ways
    
    total_squared = 0
    for i in range(1,101):
        total_squared += i**2
        
    total_sum = 0
    for i in range(1,101):
        total_sum += i
        
    result = total_sum**2 - total_squared
    
    print("Result: {}".format(result))
    
    
if __name__ == "__main__":
    main()