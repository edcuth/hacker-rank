#Find a string
#https://www.hackerrank.com/challenges/find-a-string
def count_substring(string, sub_string):
    count = 0
    for x in range(len(string) - len(sub_string) + 1):
        if string[x:x+len(sub_string)] == sub_string:
            count += 1
    return count

