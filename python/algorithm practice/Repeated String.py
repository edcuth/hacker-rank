#Repeated String
#https://www.hackerrank.com/challenges/repeated-string
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = s.count("a")
    return (count * int(n / len(s))) + int(s.count("a", 0, n%len(s)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
