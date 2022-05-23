dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(rows, columns, queries):
    answer = []
    graph = makeGraph(rows, columns)
    for x1, y1, x2, y2 in queries:
        answer.append(rotate(graph, x1, y1, x2, y2))
    return answer


def rotate(graph, x1, y1, x2, y2):
    x1 -= 1; y1 -= 1; x2 -=1 ; y2 -= 1;
    i = 0
    x, y = x1, y1
    nx, ny = x + dx[i], y + dy[i]
    min_value = graph[x1][y1]
    value = graph[x1][y1]
    while(1):
        graph[nx][ny], value = value, graph[nx][ny]
        if value < min_value:
            min_value = value
        if x1 <= nx + dx[i] <= x2 and y1 <= ny + dy[i] <= y2:
            nx, ny = nx + dx[i], ny + dy[i]
        else:
            i = (i + 1) % 4
            nx, ny = nx + dx[i], ny + dy[i]
        if nx == x1 and ny == y1:
            graph[nx][ny] = value
            break
    return min_value


# done
def makeGraph(rows, columns):
    graph = [[0] * columns for _ in range(rows)]
    count = 1
    x, y = 0, 0
    while(count <= rows * columns):
        graph[x][y] = count
        count += 1
        y += 1
        if y == columns:
            x += 1
            y = 0
    return graph
