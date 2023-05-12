from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while 1:
            mid = (left + right) // 2
            if nums[left] > nums[right]:
                if nums[left] <= nums[mid]:
                    left = mid + 1
                elif nums[left] > nums[mid]:
                    right = mid

            if nums[left] <= nums[right]:
                return nums[left]


print(Solution().findMin([3,4,5,1,2])) # 1
print(Solution().findMin([4,5,6,7,0,1,2])) # 0
print(Solution().findMin([11,13,15,17])) # 11
print(Solution().findMin([10,12,0,1,2])) # 0
print(Solution().findMin([0,1])) # 0
print(Solution().findMin([1,0])) # 0
print(Solution().findMin([0])) # 0

