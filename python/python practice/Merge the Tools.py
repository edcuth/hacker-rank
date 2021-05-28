#Merge the Tools
#https://www.hackerrank.com/challenges/merge-the-tools
def merge_the_tools(string, k):
    # your code goes here
    for s in range(0, len(string), k):
        a = []
        for b in range(s, s+k):
            if string[b] not in a:
                a.append(string[b])
        print("".join(a))
