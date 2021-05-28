#collections.Counter()
#https://www.hackerrank.com/challenges/collections-counter
from collections import Counter
x = int(input())
arr = map(int, input().split())
arr = Counter(arr)
c = int(input())
total = 0
for x in range(c):
    size, pay = map(int, input().split())
    if arr[size] > 0:
        arr[size] -= 1
        total += pay
print(total)
