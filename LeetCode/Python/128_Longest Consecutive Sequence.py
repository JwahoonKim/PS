from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        answer = 0
        for n in num_set:
            if n - 1 in num_set:
                continue

            tmp = 1
            y = n + 1
            while y in num_set:
                tmp += 1
                y += 1
            answer = max(answer, tmp)

        return answer