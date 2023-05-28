from typing import List


def helper(left, right, cuts, memo, cuts_dict):
    if not cuts:
        return 0

    if memo[cuts_dict[left]][cuts_dict[right]] != -1:
        return memo[cuts_dict[left]][cuts_dict[right]]

    result = int(1e9)
    for i in range(len(cuts)):
        now_cut = right - left
        left_cut = helper(left, cuts[i], cuts[:i], memo, cuts_dict)
        right_cut = helper(cuts[i], right, cuts[i + 1:], memo, cuts_dict)
        result = min(result, now_cut + left_cut + right_cut)

    memo[cuts_dict[left]][cuts_dict[right]] = result
    return result


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts_dict = dict({0: 0, n: len(cuts) + 1})
        for i, c in enumerate(cuts):
            cuts_dict[c] = i + 1

        memo = [[-1] * (len(cuts) + 2) for _ in range(len(cuts) + 2)]
        return helper(0, n, cuts, memo, cuts_dict)
