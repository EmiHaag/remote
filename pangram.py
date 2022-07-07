#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    phraseLower = s.lower()

    for c in phraseLower:
        ind = -1
        try:
            ind = arr.index(c)
        except ValueError:
            print(c, " not found in array list")
      
        if ind > -1:
            arr.pop(ind)
    
    if len(arr) > 0:
       return "not pangram"
    else: return "pangram"
   
s = "We promptly judged antique ivory buckles for the next prize"
print(pangrams(s))
