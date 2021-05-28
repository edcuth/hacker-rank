#Connected Cells in a Grid
#https://www.hackerrank.com/challenges/connected-cell-in-a-grid/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
def fast_find_union(matrix):
    """
    Using find union model to solve the problem
    This implementation avoids the recursive method. Besides, it is believed to be super efficient for larger problems
    :param matrix: input matrix
    :return: num of connected area
    """
    n_row = len(matrix)
    n_col = len(matrix[0])
    total_size = n_row * n_col
    id_list = list()
    sz_list = list()

    # initialize
    # each node is its own root
    # each tree has the size of 1
    for i in range(0,total_size):
        id_list.append(i)
        sz_list.append(1)

    # define find function
    def root(i):
        while i!=id_list[i]:
            # Path compression, this is not necessary, but it helps flatting the structure
            id_list[i] = id_list[id_list[i]]
            # original find func
            i = id_list[i]
        return i

    # define union function
    def union(p, q):
        i = root(p)
        j = root(q)
        if i==j:
            return
        # the size list help to balance each tree (the smaller branch get attached to the larger )
        if sz_list[i]<sz_list[j]:
            id_list[i] = j
            sz_list[j] += sz_list[i]
        else:
            id_list[j] = i
            sz_list[i] += sz_list[j]

    # define is_connected function
    def is_connected(p, q):
        return root(p) == root(q)

    # this is the service function to solve current problem
    def main(matrix):
        for row in range(0,n_row):
            for col in range(0,n_col):
                index = row*n_col + col
                value = matrix[row][col]
                if value ==1:
                    # when scanned in this way( from up-left to right-down), you only need to watch out four direction
                    if row+1<n_row and matrix[row+1][col]==1:
                        union(index, (row+1)*n_col + col)
                    if col+1<n_col and matrix[row][col+1]==1:
                        union(index, row * n_col + col+1)
                    if row+1<n_row and col+1<n_col and matrix[row+1][col+1]==1:
                        union(index, (row+1) * n_col + col + 1)
                    if row+1<n_row and col-1>=0 and matrix[row+1][col-1]==1:
                        union(index, (row+1) * n_col + col - 1)
        # after union all of them, the max area is already kept inside the size_list
        # we only need to find the largest value in size list
        n_max = 0
        for item in sz_list:
            if item>n_max:
                n_max=item
        return n_max


    return main(matrix)
def connectedCell(matrix):
    return fast_find_union(matrix)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
