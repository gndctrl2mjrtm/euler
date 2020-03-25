#!/bin/env/python
#-*- encoding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from __future__ import print_function, division
import tqdm


def is_palindrome(n):
    n = str(n)
    rev = n[::-1]
    return n == rev


def main():
    largest_palindrome = 0
    exit = False
    for i in tqdm.tqdm(range(1000,100, -1), desc="Checking possible numbers"):
        for j in range(1000, 100, -1):
            z = str(i*j)
            if is_palindrome(z):
                print("Found palindrome: {}".format(z))
                if int(z) > largest_palindrome:
                    largest_palindrome = int(z)
        if exit:
            break
        
    print("Result: {}".format(largest_palindrome))
    
    
if __name__ == "__main__":
    main()