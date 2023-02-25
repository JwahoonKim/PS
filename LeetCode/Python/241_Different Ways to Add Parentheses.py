from typing import List


def compute(left, right, value):
    result = []
    for l in left:
        for r in right:
            result.append(eval(str(l) + value + str(r)))
    return result


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        answer = []

        if expression.isnumeric():
            return [int(expression)]

        for idx, value in enumerate(expression):
            if value in "+-*":
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])
                answer += compute(left, right, value)

        return answer

Solution().diffWaysToCompute("2*3-4*5")