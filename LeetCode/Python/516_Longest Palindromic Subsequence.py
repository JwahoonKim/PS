def findAnswer(left, right, s, memo):
    if memo[left][right] != 0:
        return memo[left][right]

    if left == right:
        return 1

    if left > right:
        return 0

    if s[left] == s[right]:
        memo[left][right] = 2 + findAnswer(left + 1, right - 1, s, memo)
        return memo[left][right]

    memo[left][right] = max(findAnswer(left + 1, right, s, memo), findAnswer(left, right - 1, s, memo))
    return memo[left][right]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[0] * len(s) for _ in range(len(s))]
        return findAnswer(0, len(s) - 1, s, memo)


print(Solution().longestPalindromeSubseq("cbbd"))