#Luck Balance
#https://www.hackerrank.com/challenges/luck-balance
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    count = 0
    contests.sort()
    for c in reversed(contests):
        if c[1] == 1 and k>0:
            count += c[0]
            k -= 1
        elif c[1] == 0:
            count += c[0]
        else:
            count -= c[0]
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
