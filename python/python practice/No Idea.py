#No Idea
#https://www.hackerrank.com/challenges/no-idea
n, m = map(int, input().split())
arr = list(input().split())
a = set(input().split())
b = set(input().split())
count = 0
for i in arr:
    if i in a:
        count += 1
    elif i in b:
        count -= 1
print(count)
