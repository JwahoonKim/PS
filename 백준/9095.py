for i in range(int(input())):
    dp = [0, 1, 2, 4]
    for i in range(4, 12):
        dp.append(dp[-1] + dp[-2] + dp[-3])
    print(dp[int(input())])    