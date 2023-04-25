from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        arr1 = nums[1:]
        arr2 = nums[:-1]
        arr1[1] = max(arr1[0], arr1[1])
        arr2[1] = max(arr2[0], arr2[1])

        for i in range(2, len(arr1)):
            arr1[i] = max(arr1[i - 1], arr1[i - 2] + arr1[i])
            arr2[i] = max(arr2[i - 1], arr2[i - 2] + arr2[i])

        return max(max(arr1), max(arr2))