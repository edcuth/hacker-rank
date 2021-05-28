#Beautiful Triplets
#https://www.hackerrank.com/challenges/beautiful-triplets/
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    arr2 = Counter(arr)
    result = 0
    for k in arr2.keys():
        if k + d in arr2.keys():
            if k + d + d in arr2.keys():
                result += arr2[k] * arr2[k + d] * arr2[k + d+ d]
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
