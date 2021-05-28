#Anagram
#https://www.hackerrank.com/challenges/anagram/
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the anagram function below.
def anagram(s):
    if len(s) % 2 == 1:
        return -1
    x = len(s)//2
    a = Counter(s[:x])
    b = Counter(s[x:])
    return x - sum((a & b).values())
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
