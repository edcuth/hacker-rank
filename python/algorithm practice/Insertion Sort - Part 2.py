#Insertion Sort - Part 2
#https://www.hackerrank.com/challenges/insertionsort2/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        if arr[i] < max(arr[0:i]):
            for a in range(len(arr[0:i])):
                if arr[a] > arr[i]:
                    arr.insert(a, arr.pop(i))
        for x in arr:
            print(x, end=" ")
        print("")
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
