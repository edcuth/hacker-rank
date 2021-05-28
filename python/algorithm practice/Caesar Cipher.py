#Caesar Cipher
#https://www.hackerrank.com/challenges/caesar-cipher-1/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    abc = list("abcdefghijklmnopqrstuvwxyz")
    abcupper = list("abcdefghijklmnopqrstuvwxyz".upper())
    cba = list(s)
    for i in range(len(cba)):
        if cba[i] in abc or cba[i] in abcupper:
            if cba[i].isupper():
                cba[i] = abcupper[(abcupper.index(s[i]) + k) % len(abc)]
            else: cba[i] = abc[(abc.index(s[i]) + k) % len(abc)]
    return "".join(cba)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
