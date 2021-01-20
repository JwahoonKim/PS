from collections import Counter
import sys

input = sys.stdin.readline

INF = int(1e9)

n, m, b = map(int, input().split())
land2D = []
land1D = []
answerTime = INF
for i in range(n):
    land2D.append(list(map(int, input().split())))
# 2D --> 1D로
for i in land2D:
    for j in i:
        land1D.append(j)
# 각 높이의 블럭이 몇개씩 있는지 정보를 담는 count
count = sorted(dict(Counter(land1D)).items(), reverse=True)
# 땅의 높이 전부 다 해봐서 시간 제일 적게 걸리는 것 찾기
for height in range(0, 257):
    needBlock = 0
    delTime = 0
    addTime = 0
    block = b
    for now in count:
        # ex.) now = (1, 10) : 높이 1인 블럭 10개
        if now[0] == height:
            continue
        if now[0] > height:
            block += (now[0] - height) * now[1]
            delTime += 2 * (now[0] - height) * now[1]
        elif now[0] < height:
            needBlock += (height - now[0]) * now[1]
            addTime += (height - now[0]) * now[1]
    if needBlock > block:
        continue
    else:
        nowTime = addTime + delTime
        if nowTime <= answerTime:
            answerTime = nowTime
            answerHeight = height
print(answerTime, answerHeight)
