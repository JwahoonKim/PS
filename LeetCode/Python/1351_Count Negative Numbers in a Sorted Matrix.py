from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        m = len(grid)
        n = len(grid[0])
        now_row = 0
        now_col = n - 1

        while now_row < m:
            if grid[now_row][-1] >= 0:
                now_row += 1
                continue

            if now_col == 0:
                answer += (m - now_row) * n
                break

            while grid[now_row][now_col] < 0 and now_col >= 0:
                now_col -= 1

            now_col += 1
            now_row += 1
            answer += n - now_col

        return answer


print(Solution().countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(Solution().countNegatives(grid = [[7,-3]]))
