#Jumping on the Clouds: Revisited
#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    x = 0
    while True:
        x += k
        e -= 1
        if c[(x)%len(c)] == 1:
            e -= 2
        if (x) % len(c) == 0 or e <= 0:
            break
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
