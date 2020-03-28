#!/bin/env/python
#-*- encoding: utf-8 -*-
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from __future__ import print_function, division
import sys
import os


file_data = '''
#!/bin/env/python
#-*- encoding: utf-8 -*-
"""

"""
from __future__ import print_function, division


def main():
    pass
    
    
if __name__ == "__main__":
    main()
'''


def main():
    # TODO: Arg Check, Sys Check
    number = int(sys.argv[1])
    os.mkdir("problem{}".format(number))
    os.system("touch problem{}/__init__.py".format(number))
    with open("problem{}/problem{}.py".format(number, number), "w") as f:
        f.write(file_data)
    
    
if __name__ == "__main__":
    main()