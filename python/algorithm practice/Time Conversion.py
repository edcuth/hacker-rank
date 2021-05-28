#Time Conversion
#https://www.hackerrank.com/challenges/time-conversion
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[-2] == "P":
        if s[0:2] == "12":
            s = s[0:8]
        else:
            s = str(int(s[0:2]) + 12) + s[2:8]
    elif s[-2] == "A" and s[0:2] == "12":
        s = "00" + s[2:8]
    else:
        s = s[0:8]
    return s
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
