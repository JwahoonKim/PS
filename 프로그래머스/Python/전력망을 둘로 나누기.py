def go(idx, graph, visited):
    cnt = 0
    if visited[idx]:
        return 0

    visited[idx] = True

    for next_idx in graph[idx]:
        cnt += go(next_idx, graph, visited)

    return cnt + 1


def calc_diff(n, graph):
    visited = [True] + [False] * n
    one = go(1, graph, visited)
    visited[1] = True

    other = 0
    for idx, v in enumerate(visited):
        if not v:
            other = go(idx, graph, visited)
            break

    return abs(one - other)



def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for start, end in wires:
        graph[start].append(end)
        graph[end].append(start)

    answer = 100
    for start, end in wires:
        graph[start].remove(end)
        graph[end].remove(start)

        diff = calc_diff(n, graph)
        answer = min(answer, diff)

        graph[start].append(end)
        graph[end].append(start)

    return answer


solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])