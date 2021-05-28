#Picking Numbers
#https://www.hackerrank.com/challenges/picking-numbers/
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    longest = 0
    streak1 = []
    streak2 = []
    done = []
    for i in a:
        if i not in done:
            done.append(i)
            for x in a:
                if i == x + 1:
                    streak1.append(x)
                elif i == x - 1:
                    streak2.append(x)
                elif i == x:
                    streak1.append(x)
                    streak2.append(x)
            print(streak1, streak2)
            if len(streak1) > len(streak2):
                if longest < len(streak1):
                    longest = len(streak1)
            else:
                if longest < len(streak2):
                    longest = len(streak2)
            streak1 = []
            streak2 = []
    return longest
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
