#Fair Rations
#https://www.hackerrank.com/challenges/fair-rations
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    count=0
    for a in range(len(B)):
        try:
            if B[a]%2 is 1:
                count+=2
                B[a+1]+=1
        except:
            return 'NO'
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
