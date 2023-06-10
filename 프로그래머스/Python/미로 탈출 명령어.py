import sys
sys.setrecursionlimit(500000)

answer = ""


def solution(n, m, x, y, r, c, k):
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    dd = ['d', 'l', 'r', 'u']

    global answer
    answer = ""

    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    def dfs(cur_r, cur_c, path):
        global answer

        if answer:
            return

        if abs(r - cur_r) + abs(c - cur_c) > k - len(path):
            return

        if cur_r == r and cur_c == c and len(path) == k:
            answer = path
            return

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            direction = dd[i]

            if 1 <= nr <= n and 1 <= nc <= m and len(path) < k:
                dfs(nr, nc, path + direction)

    dfs(x, y, "")
    return answer


print(solution(3,4,2,3,3,1,5))
print(solution(2,2,1,1,2,2,2))
