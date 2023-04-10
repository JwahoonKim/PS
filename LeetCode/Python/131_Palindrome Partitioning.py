from typing import List


answer = []


def calc(s, path):
    global answer
    if not s:
        answer.append(path)
        return

    for i in range(1, len(s) + 1):
        if s[:i] == s[:i][::-1]:
            calc(s[i:], path + [s[:i]])


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                calc(s[i:], [s[:i]])
        return answer
