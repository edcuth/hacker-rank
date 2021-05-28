#itertools.permutations()
#https://www.hackerrank.com/challenges/itertools-permutations
from itertools import permutations
if __name__ == "__main__":
    s, k = map(str, input().split())
    for a in sorted(list(permutations(s, int(k)))):
        print("".join(a))
