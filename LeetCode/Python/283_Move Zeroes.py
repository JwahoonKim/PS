from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_cnt = 0
        cursor = 0
        for n in nums:
            if n == 0:
                zero_cnt += 1

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cursor] = nums[i]
                cursor += 1
        
        for i in range(cursor, len(nums)):
            nums[i] = 0



