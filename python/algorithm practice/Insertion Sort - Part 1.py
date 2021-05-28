#Insertion Sort - Part 1
#https://www.hackerrank.com/challenges/insertionsort1
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    a = arr[-1]
    for x in range(2, len(arr) + 1):
        if a < arr[x * -1]:
            arr[(x - 1) * -1] = arr[x * -1]
            for i in arr:
                print(i, end=" ")
            print("")
        else: 
            arr[(x-1) * -1] = a
            for i in arr:
                print(i, end=" ")
            break
    if a < arr[0]:
        arr[0] = a
        for i in arr:
            print(i, end=" ")
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
