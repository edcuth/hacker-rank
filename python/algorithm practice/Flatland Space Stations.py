#Flatland Space Stations
#https://www.hackerrank.com/challenges/flatland-space-stations/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    max_dist = 0
    c.sort()
    for x in range(1, len(c)):
        if (c[x] - c[x - 1]) // 2 > max_dist:
            max_dist = (c[x] - c[x - 1]) // 2
    if (n - 1) - c[-1] > max_dist:
        max_dist = (n - 1) - c[-1]
    if c[0] - 1 > max_dist:
        max_dist = c[0]
    return max_dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
