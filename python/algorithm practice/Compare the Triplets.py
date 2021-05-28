#Compare the Triplets
#https://www.hackerrank.com/challenges/compare-the-triplets
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_wins = 0
    b_wins = 0
    for x in range(0, len(a)):
        if a[x] < b[x]:
            b_wins += 1
        elif a[x] > b[x]:
            a_wins += 1
        else: continue
    result = [a_wins, b_wins]
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
