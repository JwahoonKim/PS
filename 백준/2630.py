import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

blue = 0
white = 0


def check(i, j, n):
    global blue, white
    color = graph[i][j]
    for x in range(i, i + n):
        for y in range(j, j + n):
            if graph[x][y] != color:
                check(i, j, n // 2)
                check(i + n // 2, j, n // 2)
                check(i, j + n // 2, n // 2)
                check(i + n // 2, j + n // 2, n // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1
    return


if __name__ == "__main__":
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    check(0, 0, n)

    print(white)
    print(blue)