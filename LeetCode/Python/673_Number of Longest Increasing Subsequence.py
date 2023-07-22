from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        m = 0
        dp = [1] * n
        freq = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        freq[i] = freq[j]
                    elif dp[i] == dp[j] + 1:
                        freq[i] += freq[j]
            m = max(m, dp[i])

        return sum(f for l, f in zip(dp, freq) if l == m)
