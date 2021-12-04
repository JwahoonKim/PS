from heapq import heappush, heappop
import sys

input = sys.stdin.readline
n = int(input())

leftPart, rightPart = [], []
leftCount, rightCount = 0, 0
midValue = 0

# 맨 처음 첫 값은 leftPart에 삽입
curNumber = int(input())
midValue = curNumber
# 최대힙 유지를 위해 음수값으로 변환해서 삽입
leftPart.append(-curNumber)
leftCount += 1
print(midValue)

for _ in range(n - 1):
    curNumber = int(input())
    # rightPart에 삽입해야하는 경우
    if curNumber >= midValue:
        # 양쪽 밸련스가 무너져 조정해야하는 경우
        if rightCount == leftCount:
            heappush(rightPart, curNumber)
            rightNumber = heappop(rightPart)
            heappush(leftPart, -rightNumber)
            leftCount += 1
        else:
            heappush(rightPart, curNumber)
            rightCount += 1

    elif curNumber < midValue:
        # 양쪽 밸련스가 무너져 조정해야하는 경우
        if leftCount - rightCount >= 1:
            leftNumber = heappop(leftPart)
            heappush(leftPart, -curNumber)
            heappush(rightPart, -leftNumber)
            rightCount += 1
        else:
            heappush(leftPart, -curNumber)
            leftCount += 1
    midValue = -leftPart[0]
    print(midValue)




