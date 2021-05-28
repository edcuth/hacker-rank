#Drawing Book
#https://www.hackerrank.com/challenges/drawing-book
#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    if n % 2 == 0:
        if p in (1, n):
            return 0
        elif p == (n - 1):
            return 1
    else:
        if abs(n - p)//2 > (p//2):
            return p//2
        else: return (n-p)//2
    if n % 2 == 1:
        if p in (1, n, n-1):
            return 0
    else:
        if abs(n - p)//2 > (p//2):
            return p//2
        else: return (n-p)//2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
