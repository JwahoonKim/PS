class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_smallest_num_index(nums):
            left, right = 0, len(nums) - 1

            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        pivot = find_smallest_num_index(nums)

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_with_offset = (mid + pivot) % len(nums)

            if nums[mid_with_offset] == target:
                return mid_with_offset
            elif nums[mid_with_offset] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    