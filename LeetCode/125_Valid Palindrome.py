class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = [c.lower() for c in s if c.isalnum()]
        return _s == _s[::-1]