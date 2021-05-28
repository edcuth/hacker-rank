#Viral Advertising
#https://www.hackerrank.com/challenges/strange-advertising
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared = 5
    total = 0
    for x in range(n):
        liked = shared // 2
        shared = liked * 3
        total += liked
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
