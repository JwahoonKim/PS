from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = int(1e9)
        answer = INF
        left, right = 0, 0
        sum = nums[0]

        while left <= right:
            if sum >= target:
                answer = min(answer, right - left + 1)
                sum -= nums[left]
                left += 1
            else:
                right += 1
                if right == len(nums):
                    break
                sum += nums[right]

        return answer if answer != INF else 0


print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
