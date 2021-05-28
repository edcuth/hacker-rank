#Making Anagrams
#https://www.hackerrank.com/challenges/making-anagrams
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    a = Counter(s1)
    b = Counter(s2)
    return (len(s1) + len(s2)) - (sum((a & b).values()))*2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
