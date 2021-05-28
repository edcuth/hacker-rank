#Encryption
#https://www.hackerrank.com/challenges/encryption
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    c = math.ceil(math.sqrt(len(s)))
    result = ""
    for i in range(c):
        result += (s[i::c] + ' ')
        print(i, c, s[i::c])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
