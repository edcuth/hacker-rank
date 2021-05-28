#Sales by Match
#https://www.hackerrank.com/challenges/sock-merchant
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    counted = []
    odds = 0
    for i in ar:
        if i not in counted:
            counted.append(i)
            odds += int(ar.count(i) / 2)
    return odds

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
