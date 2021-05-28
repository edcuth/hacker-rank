#Capitalize
#https://www.hackerrank.com/challenges/capitalize
def solve(s):
    s = list(s)
    if s[0].isalpha():
        s[0] = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == " ":
            s[i] = s[i].upper()
    return "".join(s)
