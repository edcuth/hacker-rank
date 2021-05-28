#Check Subset
#https://www.hackerrank.com/challenges/py-check-subset
if __name__ == '__main__':
    cases = int(input())
    
    for case in range(cases):
        len_a = int(input())
        a = set(input().split())
        len_b = int(input())
        b = set(input().split())
        if a.issubset(b):
            print("True")
        else: print("False")
