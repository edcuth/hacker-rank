#Divisible Sum Pairs
#https://www.hackerrank.com/challenges/divisible-sum-pairs
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    pairs = 0
    for j in range(0, n):
        for i in range(j):
            if (ar[i] + ar[j]) % k == 0:
                pairs += 1
    print(pairs)
    return pairs
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
