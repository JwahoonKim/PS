def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                time += 1
            else:
                time += 1
                break
        answer.append(time)
    return answer
