#Quicksort 1 - Partition
#https://www.hackerrank.com/challenges/quicksort1/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    left = []
    right = []
    equal = arr[0]
    for a in arr[1:]:
        if a > equal:
            right.append(a)
        elif a < equal:
            left.append(a)
    return left + [equal] + right
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
