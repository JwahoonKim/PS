import sys
readline = sys.stdin.readline

n = int(input())
day = [0] * n
money = [0] * n
dp = [0] * (n + 1)
for i in range(n):
    day[i], money[i] = map(int, readline().split())

for i in range(n):
    if  (i + day[i]) <= n:
        #i 번째 일을 골랐을 경우, 안골랐을 경우
        choice = dp[i] + money[i]
        not_choice = dp[i + day[i]]
        dp[i + day[i]] = max(choice, not_choice)
    # #영향을 못받은 dp[i + 1] 은 dp[i] 와 같다. 영향을 받았는 지 못받았는지 체크하는 코드
    # 이 코드 별론듯 수정좀
    dp[i + 1] = max(dp[i + 1], dp[i])
    
print(dp[n])
