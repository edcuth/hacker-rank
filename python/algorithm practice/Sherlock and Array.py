#Sherlock and Array
#https://www.hackerrank.com/challenges/sherlock-and-array
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    # Complete this function
    summy = sum(arr)
    l = len(arr)
    left = 0
    for i in range(len(arr)):
        current=arr[i]
        summy -= current
        if left == summy:
            return 'YES'
        left += current
    return 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
