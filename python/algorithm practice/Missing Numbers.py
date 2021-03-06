#Missing Numbers
#https://www.hackerrank.com/challenges/missing-numbers
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    a = Counter(arr)
    b = Counter(brr)
    result = []
    for key in b:
        if key not in a:
            result.append(key)
        else:
            if b[key] > a[key]:
                result.append(key)
    return sorted(result)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
