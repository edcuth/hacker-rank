#Cavity Map
#https://www.hackerrank.com/challenges/cavity-map/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    print(grid)
    for g in range(1, len(grid)-1):
        grid[g] = list(grid[g])
        for i in range(1, len(grid[g]) - 1):
            if grid[g][i] > grid[g + 1][i] and grid[g][i] > grid[g - 1][i] and grid[g][i] > grid[g][i + 1] and grid[g][i] > grid[g][i - 1]:
                grid[g][i] = "X"
    for g in range(len(grid)):
        grid[g] = "".join(grid[g])
    print(grid)
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
