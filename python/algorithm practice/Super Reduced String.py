#Super Reduced String
#https://www.hackerrank.com/challenges/reduced-string/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    a = list(s)
    i = 0
    while i < len(a) - 1:
        while a[i] == a[i + 1]:
            a.pop(i)
            a.pop(i)
            i = 0
            if len(a) == 0:
                return "Empty String"
        i += 1    
    return "".join(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
