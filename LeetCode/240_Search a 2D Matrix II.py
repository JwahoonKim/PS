class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binaray_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (right + left) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False
        
        for arr in matrix:
            if binaray_search(arr, target):
                return True
        return False