#Migratory Birds
#https://www.hackerrank.com/challenges/migratory-birds
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr.sort()
    highest = 0
    count = 0
    counted = []
    for i in arr:
        if i not in counted:
            counted.append(i)
            if arr.count(i) > count:
                count = arr.count(i)
                highest = i
    return highest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
