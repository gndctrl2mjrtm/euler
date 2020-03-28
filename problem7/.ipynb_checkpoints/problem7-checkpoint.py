
#!/bin/env/python
#-*- encoding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from __future__ import print_function, division


def main():
    primes = [2]
    i = 3
    while True:
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
                
        if is_prime == True:
            primes.append(i)
        i += 1
        if len(primes) == 10001:
            break
    result = primes[-1]
    print("Result: {}".format(result))
    
    
if __name__ == "__main__":
    main()
