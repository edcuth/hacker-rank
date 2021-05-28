#itertools.combinations_with_replacement()
#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
from itertools import combinations_with_replacement
if __name__ == "__main__":
    s, k = map(str, input().split())
    s = list(s)
    s.sort()
    for a in list(combinations_with_replacement(s, int(k))):
        print("".join(a))
