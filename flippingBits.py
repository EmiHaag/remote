#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    nTo32 =format(n,'b').zfill(32)
    resInversion = '' 
    for i in nTo32:
      if i == '0': resInversion += '1'
      else: resInversion += '0'
    result = int(resInversion, 2)
    return result
        

if __name__ == '__main__':
    

    print(flippingBits(0))
