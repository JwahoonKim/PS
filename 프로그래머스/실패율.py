def solution(N, stages):
    answer = []
    totalPeople = len(stages)
    failRates = [0] * (N + 1)
    # 각 스테이지마다 몇 명 있는지 체크
    for stage in stages:
        # 막판까지 다 깬 사람은 실패율에 영향 안줘
        if stage == N + 1:
            continue
        failRates[stage] += 1

    # 단계마다 실패율 체크
    for i in range(1, N + 1):
        curPeople = failRates[i]
        if totalPeople == 0:
            break
        failRates[i] = (failRates[i] / totalPeople, i)
        totalPeople -= curPeople
    # totalPeople이 0이 되어 실패율을 비율꼴로 나타내지 못한 요소들 처리
    for i in range(N + 1):
        if failRates[i] == 0:
            failRates[i] = (0, i)

    # 실패율 내림차순 정리
    failRates = sorted(failRates, key=lambda x: (-x[0], x[1]))
    for i in range(N + 1):
        stage = failRates[i][1]
        if stage == 0:
            continue
        answer.append(stage)
    return answer
