#Bill Division
#https://www.hackerrank.com/challenges/bon-appetit/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.pop(k)
    if sum(bill) / 2 == b:
        print("Bon Appetit ")
    else:
        print(int(b - (sum(bill) / 2)))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
