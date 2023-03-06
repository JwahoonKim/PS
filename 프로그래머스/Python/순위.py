INF = int(1e9)


def solution(n, results):
    graph = [[INF] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0

    for winner, looser in results:
        graph[looser - 1][winner - 1] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    in_and_out_set = [[set(), set()] for _ in range(n)]

    for cur_node_idx, distances in enumerate(graph):
        for other_node_idx, dist in enumerate(distances):
            if dist != INF and dist != 0:
                in_and_out_set[cur_node_idx][1].add(other_node_idx)
                in_and_out_set[other_node_idx][0].add(cur_node_idx)

    answer = 0
    for in_set, out_set in in_and_out_set:
        if len(in_set) + len(out_set) == n - 1:
            answer += 1

    return answer
