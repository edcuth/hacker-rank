#Nested Lists
#https://www.hackerrank.com/challenges/nested-list
if __name__ == '__main__':
    name_score = []
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score.append([score, name])
        score_list.append(score)
    score_list = list(set(score_list))
    score_list.sort()
    name_score.sort()
    name_score.reverse()
    for s in name_score:
        if s[0] == score_list[1]:
            name_list.append(s[1])
        elif s[0] < score_list[1]:
            break
    name_list.sort()
    for n in name_list:
        print(n)
