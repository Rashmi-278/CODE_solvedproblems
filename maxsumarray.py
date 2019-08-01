#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below. non - adjacent 
def maxSubsetSum(arr):
    incl = arr[0]
    excl = 0

    previncl = incl
    prevexcl = excl

    for i in range(1,len(arr)):
        incl = excl + arr[i]
        excl = max(prevexcl,previncl)

        previncl = incl
        prevexcl = excl
    return max(incl,excl)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
