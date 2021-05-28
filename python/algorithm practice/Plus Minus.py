#Plus Minus
#https://www.hackerrank.com/challenges/plus-minus
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    zero = 0
    neg = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg +=  1
        else:
            zero += 1
    print(float(pos/len(arr)))
    print(float(neg/len(arr)))
    print(float(zero/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
