

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
    pos_count = 0
    neg_count = 0
    zero_count = 0
    
    for i in arr:
        if i > 0:
            pos_count+=1
        elif i < 0:
            neg_count += 1
        else:
            zero_count += 1
    n = len(arr)
    print(round(pos_count/n,6))
    print(round(neg_count/n,6))
    print(round(zero_count/n,6))
            
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
