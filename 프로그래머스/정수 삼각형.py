def solution(triangle):
    h = len(triangle)
    for floor in range(1, h):
        for j in range(len(triangle[floor])):
            if j == 0:
                triangle[floor][j] += triangle[floor - 1][0]
            elif j == len(triangle[floor]) - 1:
                triangle[floor][j] += triangle[floor - 1][-1]
            else:
                compare = max(triangle[floor - 1][j - 1], triangle[floor - 1][j])
                triangle[floor][j] += compare
    return max(triangle[h - 1])
