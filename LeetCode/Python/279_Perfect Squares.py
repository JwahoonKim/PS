INF = int(1e9)


def calc(n, memo):
    if memo[n] != INF:
        return memo[n]

    i = 1
    while n - i * i > 0:
        memo[n] = min(1 + calc(n - i * i, memo), memo[n])
        i += 1

    return memo[n]


class Solution:
    def numSquares(self, n: int) -> int:
        memo = [INF] * (n + 1)

        i = 1
        while i * i <= n:
            memo[i * i] = 1
            i += 1

        return calc(n, memo)
