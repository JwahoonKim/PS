def solution(routes):
    answer = 0
    # 나가는 시점을 기준으로 오름차순 정렬
    routes = sorted(routes, key=lambda x: x[1])
    # visited = [False] * len(routes)
    camera = -30001
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]

    # for i in range(len(routes)):
    #     # 이미 카메라에 찍힌 자동차라면 넘어가
    #     if routes[i][0] > camera:
    #         answer += 1
    #         camera = routes[i][1]

    #     if visited[i] == True:
    #         continue
    #     else:
    #         # 나가는 지점에 카메라 설치(최적선택)
    #         answer += 1
    #         camera = routes[i][1]
    #         # 방금 설치한 카메라 위치로 커버할 수 있는 자동차들 체크
    #         for j in range(i + 1, len(routes)):
    #             if routes[j][0] <= camera <= routes[j][1]:
    #                 visited[j] = True
    return answer


if __name__ == "__main__":
    routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
    print(solution(routes))