def solution(lines):
    answer = 0
    logs = []
    # 시작시간과 끝시간을 초로 변환하여 logs에 담음
    for line in lines:
        time = line.split(" ")[1]
        howLong = float(line.split(" ")[2][:-1])
        seperatedTime = time.split(":")
        timeBySec = (
            int(seperatedTime[0]) * 3600
            + int(seperatedTime[1]) * 60
            + float(seperatedTime[2])
        )
        start = round(timeBySec - howLong + 0.001, 4)
        end = timeBySec
        logs.append([start, end])

    # 단속카메라 문제와 같은 방식으로 풀이
    for i in range(len(logs)):
        result = 1
        cur = logs[i][1]
        for j in range(i + 1, len(logs)):
            if logs[j][0] < cur + 1:
                result += 1
        answer = max(answer, result)
    return answer
