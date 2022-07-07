#!/bin/python3

from lib2to3.pgen2.token import AMPER
import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    isAM = True if s[-2:] == "AM" else False
    hour = int(s[:2])
    horaResult = ''
    print(s[2:-2])

    if(isAM):
        if(hour == 12):
            horaResult = "00"
            print("00 24h")
        else:
            horaResult = s[:2]
            print(s[:2]," 24h")
    else:
        #is PM
        if(hour == 12):
            horaResult="12"
            print("12 24h")
        else:
            horaResult=str(hour + 12)
            print(str(hour + 12), " 24h")
    horaResult += s[2:-2]
    return horaResult        


if __name__ == '__main__':
  

    timeConversion('07:05:45PM')

  
