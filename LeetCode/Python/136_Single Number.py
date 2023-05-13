from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appear = set()

        for n in nums:
            if n in appear:
                appear.remove(n)
            else:
                appear.add(n)

        return appear.pop()
