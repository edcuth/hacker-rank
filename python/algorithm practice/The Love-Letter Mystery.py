#The Love-Letter Mystery
#https://www.hackerrank.com/challenges/the-love-letter-mystery
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    a = list(s)
    count = 0
    for i in range(len(s) // 2):
        count += abs(ord(a[i]) - ord(a[-1 - i]))
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
