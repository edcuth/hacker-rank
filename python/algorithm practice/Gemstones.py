#Gemstones
#https://www.hackerrank.com/challenges/gem-stones
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the gemstones function below.
def gemstones(arr):
    b = []
    for i in range(len(arr)):
        arr[i] = list(set(arr[i]))
    for x in arr:
        for z in x:
            b.append(z)
    a = Counter(b)
    count = 0
    for x in a.values():
        if x == len(arr):
            count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
