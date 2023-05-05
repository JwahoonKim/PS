from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        acc_sum = 0
        acc_sum_dict = {0: 1}

        for n in nums:
            acc_sum += n
            if acc_sum - k in acc_sum_dict:
                answer += acc_sum_dict[acc_sum - k]

            if acc_sum in acc_sum_dict:
                acc_sum_dict[acc_sum] += 1
            else:
                acc_sum_dict[acc_sum] = 1

        return answer
