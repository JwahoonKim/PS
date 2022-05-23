data1 = input()
data2 = input()

len1 = len(data1)
len2 = len(data2)

dp = [[0] * (len1 + 1) for _ in range(len2 + 1)]

for i in range(1, len2 + 1):
    for j in range(1, len1 + 1):
        now = data2[i - 1]
        if now == data1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
