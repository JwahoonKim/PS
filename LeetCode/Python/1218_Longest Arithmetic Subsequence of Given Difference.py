from collections import defaultdict
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for n in arr:
            dp[n] = 1 + dp[n - difference]
        return max(dp.values())
