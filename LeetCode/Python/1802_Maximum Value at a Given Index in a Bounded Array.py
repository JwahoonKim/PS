def calc(value, count):
    startValue = value - 1

    if startValue >= count:
        return (count * (2 * startValue + 1 - count)) // 2
    else:
        return (startValue * (startValue + 1)) // 2 + (count - startValue)


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        answer = 1
        leftCount = index
        rightCount = n - index - 1

        left = 1
        right = maxSum
        while left <= right:
            mid = (left + right) // 2
            totalSum = mid + calc(mid, leftCount) + calc(mid, rightCount)
            if totalSum == maxSum:
                return mid
            elif totalSum < maxSum:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer


# print(Solution().maxValue(3, 2, 18)) # 7
# print(Solution().maxValue(8, 7, 14)) # 4
print(Solution().maxValue(4, 0, 4)) # 1

