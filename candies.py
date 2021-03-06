#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):

    candies = [1] * n

    for i in range(1, n):
        if arr[i - 1] < arr[i]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if arr[i + 1] < arr[i]:
            if i - 1 >= 0 and arr[i - 1] < arr[i]:
                candies[i] = max(candies[i + 1], candies[i - 1]) + 1
            else:
                candies[i] = candies[i + 1] + 1

    return(sum(candies))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
