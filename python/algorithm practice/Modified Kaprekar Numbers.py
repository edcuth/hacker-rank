#Modified Kaprekar Numbers
#https://www.hackerrank.com/challenges/kaprekar-numbers
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    result = []
    if p <= 1:
        result.append(1)
    for x in range(p, q + 1):
        d = str(x ** 2)
        if len(d) > 1:
            if int(d[len(d)//2:]) + int(d[:len(d)//2]) == x:
                result.append(x)
    if len(result) == 0:
        print("INVALID RANGE")
    else:
        for x in result:
            print(x, end=" ")
        

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
