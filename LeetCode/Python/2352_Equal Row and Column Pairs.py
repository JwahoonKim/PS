from collections import Counter, defaultdict
from typing import List


def get_col_counter(grid):
    col_info_counter = defaultdict(int)
    for i in range(len(grid)):
        col_arr = []
        for j in range(len(grid[0])):
            col_arr.append(grid[j][i])

        col_info_counter[tuple(col_arr)] += 1
    return col_info_counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        answer = 0
        row_info_counter = Counter(map(tuple, grid))
        col_info_counter = get_col_counter(grid)

        for k, v in col_info_counter.items():
            if k in row_info_counter:
                answer += row_info_counter[k] * v

        return answer
