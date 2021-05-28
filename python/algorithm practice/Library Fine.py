#Library Fine
#https://www.hackerrank.com/challenges/library-fine
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    return_date = [d1, m1, y1]
    due_date = [d2, m2, y2]
    if return_date[2] == due_date[2]:
        if return_date[1] < due_date[1]:
            return 0
        elif return_date[1] == due_date[1]:
            if return_date[0] <= due_date[0]:
                return 0
    if return_date[2] < due_date[2]:
        return  0
    elif return_date[1:3] == due_date[1:3] and return_date[0] > due_date[0]:
        return (return_date[0] - due_date[0]) * 15
    elif return_date[2] == due_date[2] and return_date[1] > due_date[1]:
        return (return_date[1] - due_date[1]) * 500
    elif return_date[2] > due_date[2]:
        return 10000

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
