
#!/bin/env/python
#-*- encoding: utf-8 -*-
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from __future__ import print_function, division
import tqdm


def main():
    # There is a faster way to generate primes, this takes way too long
    primes = [2]
    for i in tqdm.tqdm(range(3,2000000), desc="Gathering primes"):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime == True:
            primes.append(i)
    
    result = sum(primes)
    print("Result: {}".format(result))
    
    
if __name__ == "__main__":
    main()
