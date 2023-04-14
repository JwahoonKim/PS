class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair_dict = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack.pop() != pair_dict[c]:
                    return False

        return not stack


print(Solution().isValid("()[]{}"))