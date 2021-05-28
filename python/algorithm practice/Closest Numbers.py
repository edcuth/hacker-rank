#Closest Numbers
#https://www.hackerrank.com/challenges/closest-numbers
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    m = min(abs(arr[i] - arr[i+1]) for i in range(len(arr)-1))
    result = []
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i+1]) == m:
            result.append(arr[i])
            result.append(arr[i+1])
    return result 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
