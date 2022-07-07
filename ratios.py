#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here

    
    positives = round(len(list(filter(lambda n: n > 0 and n <= 100 and n >= -100, arr))) / len(arr), 6)
    negatives = round(len(list(filter(lambda n: n < 0 and n <= 100 and n >= -100, arr))) / len(arr), 6)
    print(format(positives,'.6f'))
    print(format(negatives,'.6f'))
   
   
    if arr.count(0) > 0:
        print(format(round(arr.count(0)/len(arr), 6),'.6f'))
    else:
        print(arr.count(0))

    


 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
