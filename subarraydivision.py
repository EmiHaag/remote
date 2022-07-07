import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def birthday(s, d, m):
    ways = 0
    ind = 0
    # avanzar en el array de a segmentos == m
    while (ind + m) <= (len(s)):
     
        suma = 0

        for i in range(ind, ind + m):
            print("Analizando tupla: ", s[ind:ind + m])
            if (ind + m) > (len(s)) : return ways
            suma += s[i]
          
           
        if suma == d : ways += 1
        ind += 1
    return ways


print("ways: " , birthday([2, 2, 1, 3, 2], 4, 2))
#print("ways: " , birthday([4], 4, 1))
