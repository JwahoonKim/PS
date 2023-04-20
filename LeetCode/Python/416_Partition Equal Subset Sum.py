from typing import List


def calc(target, nums, cursor, memo):
    if target == 0:
        return True

    if target < 0 or cursor >= len(nums):
        return False

    if memo[target][cursor] != -1:
        return memo[target][cursor]

    value = nums[cursor]
    memo[target][cursor] = calc(target, nums, cursor + 1, memo) or calc(target - value, nums, cursor + 1, memo)
    return memo[target][cursor]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False

        if len(nums) == 1:
            return False

        target = nums_sum // 2
        memo = [[-1] * (len(nums)) for _ in range(target + 1)]
        return calc(target, nums, 1, memo) or calc(target - nums[0], nums, 1, memo)


print(Solution().canPartition(nums = [1,5,11,5]))