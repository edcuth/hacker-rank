#sWAP cASE
#https://www.hackerrank.com/challenges/swap-case
def swap_case(s):
    x = ""
    for l in s:
        if l.isupper() == True:
            x += l.lower()
        else:
            x += l.upper()
    return x

