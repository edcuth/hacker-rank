#Ice Cream Parlor
#https://www.hackerrank.com/challenges/icecream-parlor
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    for a in range(len(arr) - 1):
        for b in range(a + 1, len(arr)):
            if arr[a]+arr[b]== m:
                return [a+1, b+1]
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
