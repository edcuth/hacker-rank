#The Minion Game
#https://www.hackerrank.com/challenges/the-minion-game
def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] in set("AEIOU"):
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin > stuart:
        print("Kevin " + str(kevin))
    elif stuart > kevin:
        print("Stuart " + str(stuart))
    else:
        print("Draw")
