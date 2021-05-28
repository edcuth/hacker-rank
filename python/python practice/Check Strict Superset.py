#Check Strict Superset
#https://www.hackerrank.com/challenges/py-check-strict-superset
if __name__ == '__main__':
    a = set(input().split())
    print(all(a > set(input().split()) for _ in range(int(input()))))
