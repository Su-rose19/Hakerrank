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
    # Write your code here
    sum = 0;
    arr.sort();
    for i in arr:
        sum = sum + i;
        #print(sum)
    #print(sum)
    print(sum-arr[4], sum-arr[0])
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
