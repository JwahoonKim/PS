import sys
#변수 입력 받기
n = int(input())
dp = [0] * 301
score = [0] * 301

#계단 점수 입력
for i in range(1, n + 1):
    score[i] = int(sys.stdin.readline())

#계단이 1,2개 인 경우
dp[1] = score[1]
dp[2] = score[1] + score[2]

# 계단이 3개 이상인 경우
for i in range(3, n + 1):
    way1 = dp[i - 2] + score[i]
    way2 = dp[i - 3] + score[i - 1] + score[i]
    dp[i] = max(way1 , way2)

print(dp[n])