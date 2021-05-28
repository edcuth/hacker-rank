#Counting Sort 1
#https://www.hackerrank.com/challenges/countingsort1
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    o = [0] * 100
    print(max(arr))
    for a in arr:
        o[a] += 1
    print(o)
    return o

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
