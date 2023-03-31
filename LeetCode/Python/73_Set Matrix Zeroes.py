from typing import List


def makeRowZero(r, matrix):
    for i in range(len(matrix[0])):
        matrix[r][i] = 0


def makeColZero(c, matrix):
    for i in range(len(matrix)):
        matrix[i][c] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_place = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_place.append([i, j])

        for r, c in zero_place:
            makeRowZero(r, matrix)
            makeColZero(c, matrix)


Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])