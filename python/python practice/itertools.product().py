#itertools.product()
#https://www.hackerrank.com/challenges/itertools-product
from itertools import product
if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = product(a, b)
    for i in c:
        print(i, end=" ")
