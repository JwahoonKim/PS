def solution(N, target):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        num = int(str(N) * i)
        dp[i].add(num)

    for i in range(1, 9):
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        if target in dp[i]:
            return i
    return -1


print(solution(5, 5))