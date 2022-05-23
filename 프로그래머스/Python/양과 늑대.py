# 현재 위치에서 갈 수 있는 노드 찾기
def getCanGoEdges(i, prev, graph):
    canGoEdges = [edge for edge in prev if edge != i]
    for j in range(len(graph)):
        if graph[i][j] == True:
            canGoEdges.append(j)
    return canGoEdges

# 현재 위치(i) 기준으로 갈 수 있는 곳 가보기 -> DFS
def DFS(i, s, w, prev, graph, info):
    global answer
    canGoEdges = getCanGoEdges(i, prev, graph)
    if s == w or not canGoEdges:
        if answer < s:
            answer = s
        return
    for edge in canGoEdges:
        if info[edge] == 0: # 가려는 노드에 양이 있는 경우
            DFS(edge, s + 1, w, canGoEdges, graph, info)
        else: # 가려는 노드에 늑대가 있는 경우
            DFS(edge, s, w + 1, canGoEdges, graph, info)

def solution(info, edges):
    global answer
    answer = 1
    graph = [[False] * len(info) for _ in range(len(info))]
    for x, y in edges:
        graph[x][y] = True
    DFS(0, 1, 0, [0], graph, info)
    return answer