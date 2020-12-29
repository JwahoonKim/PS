triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][0]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                left = triangle[i - 1][j - 1]
                right = triangle[i - 1][j]
                triangle[i][j] += max(left, right)

    print(max(triangle[len(triangle) - 1]))
    return max(triangle[len(triangle) - 1])


solution(triangle)
print(triangle)