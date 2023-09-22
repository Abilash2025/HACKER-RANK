#!/bin/python3

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
    hour = int(s[0:2])
    minutes = int(s[3:5])
    seconds = int(s[6:8])
    
    if "pm" in s.lower() and hour != 12:
        hour += 12
    elif "am" in s.lower() and hour == 12:
        hour = 0
        
    str_hour = str(hour).zfill(2)
    str_min = str(minutes).zfill(2)
    str_seconds = str(seconds).zfill(2)
        
    time = str_hour + ":" + str_min + ":" + str_seconds
    
    return time
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
