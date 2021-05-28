#Sherlock and the Valid String
#https://www.hackerrank.com/challenges/sherlock-and-valid-string
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    a = Counter(s)
    b = Counter(a.values())
    if len(b) > 2:
        return "NO"
    elif len(b) == 2:
        c = list(b.keys())
        if 1 in b.keys():
            if b[1] == 1:
                return "YES"
            else: return "NO"
        elif abs(c[0] - c[1]) == 1:
            if 1 in b.values():
                return "YES"
            else: return "NO"
        else: return "NO"
    else:
        return "YES"        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
