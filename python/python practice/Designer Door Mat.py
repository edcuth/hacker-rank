#Designer Door Mat
#https://www.hackerrank.com/challenges/designer-door-mat/
if __name__ == '__main__':
    a = input().split()
    for x in range(int(a[0])//2):
        print((".|." * (x * 2 + 1)).center(int(a[1]), "-"))
    print("WELCOME".center(int(a[1]), "-"))
    for x in range(0, int(a[0])//2):
        print((".|." * ((int(a[0])//2) * 2 - x * 2 - 1)).center(int(a[1]), "-"))
