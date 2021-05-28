#Pangrams
#https://www.hackerrank.com/challenges/pangrams
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    if len(set(s.lower())) == 27:
        return "pangram"
    else: return "not pangram"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
