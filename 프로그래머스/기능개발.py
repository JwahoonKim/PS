def solution(progresses, speeds):
    answer = []
    cursor = 0
    length = len(progresses)
    while cursor < length:
        count = 0
        for i in range(cursor, length):
            progresses[i] += speeds[i]
        for i in range(cursor, length):
            if progresses[i] < 100:
                break
            if progresses[i] >= 100:
                count += 1
                cursor += 1
        if count != 0:
            answer.append(count)
    return answer
    