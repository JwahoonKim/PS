def solution(n):
    answer = []
    snail = [[] for _ in range(n + 1)]
    cur = 1
    flag = n
    top = 1
    bottom = n
    dir = 0
    cycle = 0
    while cur <= n * (n + 1) // 2:
        # 내려가는 방향일 때
        if dir == 0:
            for floor in range(top, bottom + 1):
                snail[floor].insert(cycle, cur)
                cur += 1
            dir = (dir + 1) % 3
            top += 1

        # 오른쪽으로 가는 방향일 때
        elif dir == 1:
            i = 0
            while len(snail[bottom]) < bottom:
                snail[bottom].insert(cycle + 1 + i, cur)
                i += 1
                cur += 1
            bottom -= 1
            dir = (dir + 1) % 3
        # 위로가는 방향일 때
        else:
            for floor in range(bottom, top - 1, -1):
                if cycle == 0:
                    snail[floor].append(cur)
                    cur += 1
                # cycle = 0일때는 이상하게 들어가서
                else:
                    snail[floor].insert(-cycle, cur)
                    cur += 1
            dir = (dir + 1) % 3
            top += 1
            cycle += 1
    for i in range(1, n + 1):
        answer.extend(snail[i])
    return answer


print(solution(5))