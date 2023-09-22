#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sum_arr = []
    for i in range(0,len(arr)):
        sum = 0
        for j in range(0,len(arr)):
            if i == j:
                continue
            else:
                sum += arr[j]
        
        sum_arr.append(sum)
    
        
    print(min(sum_arr),max(sum_arr))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
