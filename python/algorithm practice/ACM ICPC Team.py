#ACM ICPC Team
#https://www.hackerrank.com/challenges/acm-icpc-team/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    print(topic)
    results = []
    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            count = 0
            for x in range(len(topic[i])):
                if topic[i][x] == "1" or topic[j][x] == "1":
                    count += 1
            results.append(count)
    print(results)
    return [max(results), results.count(max(results))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
