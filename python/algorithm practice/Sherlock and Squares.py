#Sherlock and Squares
#https://www.hackerrank.com/challenges/sherlock-and-squares
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    end = math.floor(math.sqrt(b)) + 1
    start = math.ceil(math.sqrt(a))
    return end - start
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
