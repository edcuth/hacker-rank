#Climbing the Leaderboard
#https://www.hackerrank.com/challenges/climbing-the-leaderboard
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    positions = []
    if len(ranked) == 1:
        for p in player:
            if p in ranked:
                positions.append(ranked.index(p) + 1)
        return positions
    ranked = sorted(list(set(ranked)))
    ranked.reverse()
    i = len(ranked) - 1
    for p in player:
        while i > 0:
            if p < ranked[i]:
                ranked.insert(i + 1, p)
                i += 1
                positions.append(i + 1) 
                break
            elif p == ranked[i]:
                positions.append(i + 1)
                break
            else:
                i -= 1
                if i == 0:
                    if ranked[0] > p:
                        positions.append(2)
                        i += 2
                        break
                    else:
                        positions.append(1)
                        i += 2
                        break
    print(ranked)
    return positions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
