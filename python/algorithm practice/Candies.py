#Candies
#https://www.hackerrank.com/challenges/candies
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    total = 0
    to_right = [1]
    to_left = [1]
    candy_count = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            candy_count += 1
            to_right.append(candy_count)
        else:
            candy_count = 1
            to_right.append(candy_count)
    arr.reverse()
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            candy_count += 1
            to_left.append(candy_count)
        else:
            candy_count = 1
            to_left.append(candy_count)
    to_left.reverse()
    for i in range(0, len(arr)):
        if to_right[i] >= to_left[i]:
            total += to_right[i]
        else:
            total += to_left[i]
 
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
