from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0

        for i in range(n):
            if 1 <= nums[i] % (n + 1) <= n:
                idx = (nums[i] % (n + 1)) - 1
                nums[idx] += n + 1

        for i in range(n):
            if nums[i] <= n:
                return i + 1

        return n + 1
