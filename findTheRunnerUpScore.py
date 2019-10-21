import sys


def findRunnerUpScore(num, scores):

    scoreList = list(map(int, scores.split()))        

    first = scoreList[0]
    second = scoreList[0]

    for i in range(len(scoreList)):

        if(scoreList[i] >= first):
            first = scoreList[i]


    for j in range(len(scoreList)):

        if(scoreList[j] != first):
            second = scoreList[j]


    for k in range(len(scoreList)):

        if(scoreList[k] >= second and scoreList[k] < first):
            second = scoreList[k]        

    return second

num = int(input())
scores = input()


print (findRunnerUpScore(num, scores))






