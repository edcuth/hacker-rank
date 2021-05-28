#Beautiful Binary String
#https://www.hackerrank.com/challenges/beautiful-binary-string
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    if "010" not in b:
        return 0
    a = list(b)
    count = 0
    for i in range(1, len(a) - 1):
        if a[i] == "1":
            if a[i+1] == "0":
                if a[i-1] == "0":
                    a[i+1] = "1"
                    count += 1
    return count
                
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
