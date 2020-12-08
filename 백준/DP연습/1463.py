x = int(input())
dp = [0] * (x + 1)

for i in range(2, x + 1):
    if i % 3 == 0:
        a = dp[i // 3]
    else: a = 10e7
    if i % 2 == 0:
        b = dp[i // 2]
    else : b = 10e7
    c = dp[i - 1]

    dp[i] = min(a, b, c) + 1
    
print(dp[x]) 