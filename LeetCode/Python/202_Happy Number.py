def happy(n):
    return sum(map(lambda x: int(x) ** 2, list(str(n))))


class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        while n > 1:
            history.add(n)
            n = happy(n)
            if n in history:
                return False
        return True

print(Solution().isHappy(2))