from typing import List

answer = 0


def helper(cookies, cursor, distribute):
    global answer
    if max(distribute) >= answer:
        return

    if cursor == len(cookies):
        answer = min(answer, max(distribute))
        return

    for i in range(len(distribute)):
        distribute[i] += cookies[cursor]
        helper(cookies, cursor + 1, distribute)
        distribute[i] -= cookies[cursor]


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        global answer
        answer = sum(cookies)
        helper(cookies, 0, [0] * k)
        return answer
