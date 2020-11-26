import sys

n = int(input())
# n < 3 이어도 sum[1,2,3]값이 입력되게끔 n + 3
score = [0] * (n + 3) 
for i in range(1, n + 1):
    score[i] = int(sys.stdin.readline())

#DP table 
dp = [0] * (n + 3)
# dp[n - 1]로 하면 못고르는 상태가 생김 >> dp[n - 3]으로
# dp[n - 2] 와 dp[n - 3] + score[n - 1] 을 비교해서  
# 큰 쪽을 골라 dp[greater] + score[n] = dp[n]
dp[1] = score[1]
dp[2] = score[1] + score[2]
dp[3] = max(score[1], score[2]) + score[3]
if n >= 4:
    for i in range(4, n + 1):
        if dp[i - 3] + score[i - 1] <= dp[i - 2]:
            index = i - 2
            dp[i] = dp[index] + score[i]
        else:
            index = i - 3
            dp[i] = dp[index] + score[i - 1] + score[i]
            
print(dp[n])

