from typing import List


def go(path, remain, answer, wordDict):
    if not remain:
        answer.append(path)

    for word in wordDict:
        if remain.startswith(word):
            go(path + " " + word, remain[len(word):], answer, wordDict)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        answer = []

        for word in wordDict:
            if s.startswith(word):
                go(word, s[len(word):], answer, wordDict)

        return answer
