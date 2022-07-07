#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    cursorA = 0
    cursorB = len(arr[0])-1
    sumaA = 0
    sumaB = 0
    
    for fila in arr:
        #sumamos valor de elemento actual de diagonal A y diagonal B
        sumaA += fila[cursorA] 
        sumaB += fila[cursorB]
        if cursorA < (len(fila)-1):
            cursorA += 1
            cursorB -= 1
    
    return abs(sumaA - sumaB)
    
   
   
        

if __name__ == '__main__':

    print(diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))