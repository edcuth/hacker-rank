#Angry Professor
#https://www.hackerrank.com/challenges/angry-professor
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    on_time = 0
    late = 0
    for i in range(len(a)):
        if a[i] <= 0:
            on_time += 1
    if on_time >= k:
        return "NO"
    else:
        return "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
