from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        INF = int(1e9)
        dp = [INF] * len(nums)
        dp[0] = 0

        for i, n in enumerate(nums[:-1]):
            for step in range(1, n + 1):
                if i + step < len(nums):
                    dp[i + step] = min(dp[i + step], dp[i] + 1)

        return dp[-1]

Solution().jump([2,3,1,1,4])