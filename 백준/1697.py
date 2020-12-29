#기본 : N 에서 못찾으면 N-1, N+1, 2N 중 찾아본다  >> BFS
#그렇게 뻗으면 O(3^n)이라 너무 크니 제한조건을 몇 개 준다.

from collections import deque

N,K = map(int,input().split())
sec = 0     # 몇초가 걸렸는지 체크하는 변수
flag = True   # while문을 끝낼 변수
que = deque([N])

#이미 본 곳 다시 보지않도록 visited 배열 만들어줌   #제한조건1
visited = [False] * 1000001 

while(flag): #동생 찾으면 mark = 100으로 바꿔주고 while문 끝냄
    arr = range(len(que))
    for i in arr:      
        V = que.popleft()
        visited[V] = True
        if V == K:
            flag = False
            print(sec)
        else:
            if visited[V - 1] == False and (V - 1) >= 0: # 제한조건2
                que.append(V - 1)
            if visited[V + 1] == False and (V + 1) <= 100000: # 제한조건3
                que.append(V + 1)
            if visited[V * 2] == False and (V * 2) <= 100000: # 제한조건4
                que.append(V * 2)

    sec += 1
