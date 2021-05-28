#Append and Delete
#https://www.hackerrank.com/challenges/append-and-delete
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if k >= len(s) + len(t):
        return "Yes"
    if s == t and (k % 2 == 0):
        return "Yes"
    diff = 0
    for x in range(min(len(s), len(t))):
        if s[x] != t[x]:
            del_needed = len(s) - x
            rewrites_needed = len(t) - x
            if del_needed + rewrites_needed == k or (del_needed + rewrites_needed < k and k % 2 == 0):
                return "Yes"
            else: return "No"
    if (k - abs(len(s) - len(t))) % 2 == 0:
        return "Yes"
    else: return "No"
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
