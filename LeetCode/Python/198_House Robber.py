from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for i in range(1, len(nums)):
            if i == 1:
                dp.append(max(nums[0], nums[1]))

            else:
                way1 = dp[i - 1]
                way2 = dp[i - 2] + nums[i]
                dp.append(max(way1, way2))

        return dp[-1]

