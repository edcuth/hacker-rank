#Cut the sticks
#https://www.hackerrank.com/challenges/cut-the-sticks
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    stick_count = []
    while arr != []:
        arr.sort()
        x = arr[0]
        stick_count.append(len(arr))
        for a in range(len(arr)):
            arr[a] -= x
        while 0 in arr:
            arr.remove(0)
    return stick_count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
