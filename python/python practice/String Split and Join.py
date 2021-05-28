#String Split and Join
#https://www.hackerrank.com/challenges/python-string-split-and-join
def split_and_join(line):
    # write your code here
    line = line.split()
    line = "-".join(line)
    return line
