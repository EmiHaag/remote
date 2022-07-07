#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    ret =[]
    for i in queries:
        ret.append(strings.count(i))
    return ret

if __name__ == '__main__':
    strings = ['aba','baba','aba','xzxb']
    queries = ['aba','xzxb','ab']
    res =  matchingStrings(strings, queries)
    print(res)