#itertools.combinations()
#https://www.hackerrank.com/challenges/itertools-combinations
from itertools import combinations
if __name__ == "__main__":
    s, k = map(str, input().split())
    s = list(s)
    s.sort()
    for x in range(1, int(k) + 1):
        for a in list(combinations(s, x)):
            print("".join(a))
