import sys

input = sys.stdin.readline

INF = int(1e9)

n, m, b = map(int, input().split())
land = []
time = INF
for i in range(n):
    land.append(list(map(int, input().split())))
# 가장 높은 위치부터 내려가면서 다 해보기
heightSet = set()
for i in land:
    for j in i:
        heightSet.add(j)
heightSet = sorted(heightSet, reverse=True)
# 1. 블록 개수로는 now 높이만큼 만들 수 없으면 now -= 1
# 2. 개수가 된다면 기존 time과 now에서의 time 비교해서 작은거 저장, 이때 높이도 저장
for now in heightSet:
    needBlock = 0
    delTime = 0
    block = b
    for i in range(n):
        for j in range(m):
            # now보다 높이가 높은 곳 블럭은 없애기
            if land[i][j] > now:
                block += land[i][j] - now
                delTime += 2 * (land[i][j] - now)
            # now보다 높이가 낮은 곳 높이기
            elif land[i][j] < now:
                needBlock += now - land[i][j]
    # now 높이에 맞춰서 쌓을 만큼의 block이 없을 경우 continue
    if needBlock > block:
        continue
    else:
        addTime = needBlock
        nowTime = addTime + delTime
        if nowTime < time:
            answerHeight = now
            time = nowTime

print(time, answerHeight)