from typing import List


def is_match(match_str, strs):
    for s in strs:
        if match_str != s[:len(match_str)]:
            return False
    return True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = min(strs, key=len)
        for i in range(len(s), 0, -1):
            match_str = s[:i]
            if is_match(match_str, strs):
                return match_str
        return ""