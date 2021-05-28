#HackerRank in a String!
#https://www.hackerrank.com/challenges/hackerrank-in-a-string
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    hack = list("hackerrank")
    x = 0
    for i in s:
        if i == hack[x]:
            x += 1
            if x == 10:
                return "YES"
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
