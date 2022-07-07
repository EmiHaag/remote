#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    for el in a:
        if a.count(el)==1: return el

if __name__ == '__main__':
    print(lonelyinteger([1,2,3,4,3,2,1]))