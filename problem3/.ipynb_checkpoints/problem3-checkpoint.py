#!/bin/env/python
#-*- encoding: utf-8 -*-
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from __future__ import print_function, division
import tqdm

    
def is_prime(n):
    n = int(n)
    valid = True
    for i in range(2, n):
        if n % i == 0:
            valid = False
            break
    return valid
    
    
def main():
    target = 600851475143
    limit = int(target/2)
    result = 0
    for i in tqdm.tqdm(range(2, limit), desc="Searching factors"):
        factor = target / i
        if factor % 1 == 0:
            print("-"*50)
            print("- Found factor: {}".format(factor))
            if is_prime(factor):
                print("--- Factor is prime")
                result = factor
                break
            else:
                print("-- Factor is not prime")
            
    print("Result: {}".format(int(result)))
    
    
if __name__ == "__main__":
    main()