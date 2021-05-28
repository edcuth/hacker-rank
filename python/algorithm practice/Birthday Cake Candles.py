#Birthday Cake Candles
#https://www.hackerrank.com/challenges/birthday-cake-candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort()
    tall_candles = 0
    tallest = candles[-1]
    print(tallest)
    x = 0
    for c in candles:
        x -= 1
        if candles[x] < tallest:
            break
        elif candles[x] == tallest:
            tall_candles += 1
    return(tall_candles)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
