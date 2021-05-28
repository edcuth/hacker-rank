#Stock Maximize
#https://www.hackerrank.com/challenges/stockmax
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    print(prices)
    highest  = 0
    profit = 0
    stock = 0
    cutoff = 0
    loss = 0
    while True:
        for i in prices[cutoff:len(prices)]:
            if i > highest:
                highest = i
                print(highest)
        last_cutoff = cutoff
        if highest == 0:
            break
        cutoff = prices.index(highest, cutoff)
        print(last_cutoff, cutoff)
        #loss -= prices[0]
        #stock += 1
        for i in prices[last_cutoff:cutoff]:
            if i < prices[cutoff]:
                loss -= i
                stock += 1
        profit += (prices[cutoff] * stock) + loss
        cutoff += 1
        highest = 0
        loss = 0
        stock = 0
    print(profit)
    return profit

        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
