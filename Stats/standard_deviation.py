#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def mean(arr):
    sorted_arr = sorted(arr)
    return round((sum(sorted_arr)/len(sorted_arr)), 1)

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    average_distance_sum = 0
    mean_val = mean(arr)
    for i in sorted(arr):
        average_distance_sum += pow((i-mean_val), 2)
    sd = math.sqrt(average_distance_sum/len(sorted(arr))) 
    print(round(sd, 1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
