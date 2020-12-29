import copy

def floyd_warshall(graphs):
    # floyd-warshall을 통해 최단 경로들을 저장할 새로운 그래프
    s_graph = [[INF] * N for _ in range(N)]
    # floyd-warshall algorithm
    for k in range(N):
        for a in range(N):
            for b in range(N):
                s_graph[a][b] = min(
                    graphs[a][b], graphs[a][k] + graphs[k][b])
    return s_graph


def floyd_after_delete_edge(graph, i, j):
    INF = int(1e9)

    temp_graph = copy.deepcopy(graph)
    # 간선 삭제
    temp_graph[i][j] = INF
    temp_graph[j][i] = INF

    print(temp_graph)
    after_graph = floyd_warshall(temp_graph)
    print(after_graph)
    print()
    # print(after_graph)
    flag = True
    for i in range(N):
        for j in range(N):
            if after_graph[i][j] != shortest_graph[i][j]:
                flag = False
                break
    if flag:
        print("시행")
        graph[i][j] = INF
        graph[j][i] = INF


if __name__ == "__main__":
    INF = int(1e9)
    # 도시의 수
    N = int(input())

    graph = [[] for _ in range(N)]
    # 각 간선에 대한 정보 입력받기
    for i in range(N):
        graph[i] = list(map(int, input().split()))

    shortest_graph = floyd_warshall(graph)
    if shortest_graph != graph:
        print("-1")
    else:
        for i in range(N):
            for j in range(i, N):
                if i != j:
                    floyd_after_delete_edge(graph, i, j)
    print(graph)
