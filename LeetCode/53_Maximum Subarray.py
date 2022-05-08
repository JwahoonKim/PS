class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        for i in range(1, len(nums)):
            case1 = dp[i-1] + nums[i]
            case2 = nums[i]
            dp.append(max(case1, case2))
        
        return max(dp)