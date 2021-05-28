#Marc's Cakewalk
#https://www.hackerrank.com/challenges/marcs-cakewalk
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    miles = 0
    calorie.sort(reverse=True)
    print(calorie)
    x = 0
    for i in calorie:
        miles += (2**x) * i
        x += 1
    return miles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
