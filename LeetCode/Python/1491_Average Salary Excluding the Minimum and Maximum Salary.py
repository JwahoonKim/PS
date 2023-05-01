from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        exclude_sum = sum(salary) - max(salary) - min(salary)
        return exclude_sum / (len(salary) - 2)