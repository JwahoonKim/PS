from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero_count = 0
        one_count = 0
        two_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
            elif n == 1:
                one_count += 1
            else:
                two_count += 1

        for i in range(zero_count):
            nums[i] = 0
        for i in range(zero_count, zero_count + one_count):
            nums[i] = 1
        for i in range(zero_count + one_count, zero_count + one_count + two_count):
            nums[i] = 2


Solution().sortColors([2,0,2,1,1,0])