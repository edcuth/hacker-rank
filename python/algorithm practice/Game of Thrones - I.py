#Game of Thrones - I
#https://www.hackerrank.com/challenges/game-of-thrones
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    a = Counter(s)
    if len(s) % 2 == 0:
        if all(x % 2 == 0 for x in a.values()):
            return "YES"
        else: return "NO"
    else:
        count = 0
        for x in a.values():
            if x % 2 == 1:
                count += 1
                if count == 2:
                    return "NO"
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
