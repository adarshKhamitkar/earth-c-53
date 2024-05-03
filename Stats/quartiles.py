#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def median(arr):
    size = len(arr)
    if (size % 2 == 0):
        return int((arr[int(size/2)-1]+arr[int(size/2)])/2)
    else:
        return int(arr[int(size/2)])

def quartiles(arr):
    sorted_arr = sorted(arr)
    size = len(sorted_arr)
    if(size % 2 == 0):
        first_half = sorted_arr[0:int(size/2)]
        second_half = sorted_arr[int(size/2):size]
    else:
        first_half = sorted_arr[0:int(size/2)]
        second_half = sorted_arr[int(size/2)+1:size]
    first_quartile = median(first_half)
    second_quartile = median(sorted_arr)
    third_quartile = median(second_half)
    
    quartiles = [first_quartile,second_quartile,third_quartile]
    return quartiles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
