from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        word_set = set(wordDict)

        for word in word_set:
            if s.startswith(word):
                dp[len(word) - 1] = True

        for i, v in enumerate(dp):
            if v:
                for word in word_set:
                    if s[i + 1:].startswith(word):
                        dp[i + len(word)] = True

        return dp[-1]


Solution().wordBreak("leetcode", wordDict = ["leet","code"])