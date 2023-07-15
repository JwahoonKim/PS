N = int(input())
numList = list(map(int, input().split()))
maxValue = max(numList)
numDict = dict()
for i, n in enumerate(numList):
    numDict[n] = i

score = [0] * N

for i, n in enumerate(numList):
    value = n * 2
    while value <= maxValue:
        if value in numDict.keys():
            score[i] += 1
            score[numDict[value]] -= 1
        value += n

print(' '.join(map(str, score)))