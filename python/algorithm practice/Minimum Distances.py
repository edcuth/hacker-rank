#Minimum Distances
#https://www.hackerrank.com/challenges/minimum-distances
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    min_dist = len(a) + 1
    for i in range(len(a)):
        if a[i] in a[i+1:]:
            if min_dist > abs(i - a.index(a[i], i+1)):
                min_dist = abs(i - a.index(a[i], i+1))
    if min_dist == len(a) + 1:
        return -1
    else: return min_dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
