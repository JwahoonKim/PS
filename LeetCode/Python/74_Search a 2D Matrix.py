from typing import List


def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m - 1

        while left <= right:
            mid = (left + right) // 2
            targetRow = matrix[mid]

            if targetRow[0] <= target <= targetRow[-1]:
                return binarySearch(targetRow, target) != -1
            elif target < targetRow[0]:
                right = mid - 1
            elif targetRow[-1] < target:
                left = mid + 1
            else:
                return False


print(Solution().searchMatrix([[1,3]], 3))