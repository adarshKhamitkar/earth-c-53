import math
import statistics
import scipy.stats as st
import numpy as np

def mean(arr):
    sorted_arr = sorted(arr)
    return round((sum(sorted_arr)/len(sorted_arr)), 1)
    
def median(arr):
    sorted_arr = sorted(arr)
    size = len(sorted_arr)
    if(size % 2 == 0):
        return round((sorted_arr[int(size/2)-1]+sorted_arr[int(size/2)])/2, 1)
    else:
        return round(sorted_arr[int(size/2)], 1)

def mode(arr):
    sorted_arr = sorted(arr)
    return int(statistics.mode(sorted_arr))
    
def standard_deviation(arr):
    sum_mean = 0
    sorted_arr = sorted(arr)
    size = len(sorted_arr)
    mean_arr = mean(sorted_arr)
    for i in sorted_arr:
        sum_mean+=pow((i-mean_arr), 2)
    average_mean_distance = sum_mean/size
    return round(math.sqrt(average_mean_distance), 1)
    
def confidence_interval(arr):
    sorted_arr = sorted(arr)
    intervals = st.t.interval(0.95, len(sorted_arr)-1, loc=np.mean(sorted_arr), scale=st.sem(sorted_arr))
    return list(round(x,1) for x in intervals)
    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))
    
    print(mean(vals))
    
    print(median(vals))
    
    print(mode(vals))
    
    print(standard_deviation(vals))
    
    print(confidence_interval(vals))
