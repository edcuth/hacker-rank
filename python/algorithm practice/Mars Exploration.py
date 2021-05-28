#Mars Exploration
#https://www.hackerrank.com/challenges/mars-exploration
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    x = "SOS" * (len(s) // 3)
    count  = 0
    for y in range(len(s)):
        if s[y] != x[y]:
            count += 1
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
