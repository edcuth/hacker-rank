#Equalize the Array
#https://www.hackerrank.com/challenges/equality-in-a-array
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    arr.sort()
    count = 0
    x = 0
    while x <= arr[-1]:
        if arr.count(x) > count:    
            count = arr.count(x)
            print(arr.count(x))
        x += 1
    return len(arr) - count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
