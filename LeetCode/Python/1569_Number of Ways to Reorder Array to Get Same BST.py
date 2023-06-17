import math
from typing import List


def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def helper(nums):
    if not nums:
        return 1

    root = nums[0]
    left_arr = [n for n in nums if n < root]
    right_arr = [n for n in nums if n > root]
    len_left = len(left_arr)
    len_right = len(right_arr)
    return helper(left_arr) * helper(right_arr) * comb(len_left + len_right, len_left)


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        return (helper(nums) - 1) % mod


print(Solution().numOfWays([2,1,3]))
print(Solution().numOfWays([1,2,3]))
print(Solution().numOfWays([3,4,5,1,2]))
